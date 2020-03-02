import json
import os
import boto3

bucket_mapping = {
    os.environ.get('WYDOT_TEAM_BUCKET'): os.environ.get('WYDOT_AUTOEXPORT_BUCKET')
}

def lambda_handler(event, context):
    s3_client = boto3.client('s3')
    
    source_bucket = json.loads(event['Records'][0]['Sns']['Message'])['Records'][0]['s3']['bucket']['name']
    source_key = json.loads(event['Records'][0]['Sns']['Message'])['Records'][0]['s3']['object']['key']
    
    if source_key[-1] == '/':
        print('IGNORING FILE BECAUSE IT IS A FOLDER')
        return
    
    print('Copy From: ' + source_bucket + '/' + source_key)
    print('Copy To: ' + bucket_mapping[source_bucket] + '/' + source_key[12:])
    
    try:
        s3_client.copy_object(
            Bucket = bucket_mapping[source_bucket], 
            CopySource = {'Bucket': source_bucket, 'Key': source_key}, 
            Key = source_key[12:], 
            ServerSideEncryption = 'AES256' 
            )
    except Exception as e:
        print('FAILED COPY')
        raise e
    
    print('SUCCEEDED COPY')
