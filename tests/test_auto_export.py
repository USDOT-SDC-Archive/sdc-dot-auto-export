import pytest
import boto3
import sys
from moto import mock_s3

sys.path.append('./dot-sdc-auto-export')
from dot_sdc_auto_export import lambda_function
import os

Origin_Bucket_Name = os.environ.get('WYDOT_TEAM_BUCKET')
Export_Bucket_Name = os.environ.get('WYDOT_AUTOEXPORT_BUCKET')

try:
    os.mkdir('/tmp')
except:
    pass

@mock_s3
def setup_raw_submissions():
    boto3.setup_default_session()
    conn = boto3.client('s3', region_name='us-east-1')
    conn.create_bucket(Bucket=Origin_Bucket_Name)
    conn.create_bucket(Bucket=Export_Bucket_Name)
    return conn

@mock_s3
def run_auto_export(file_path):
    key = 'auto_export/test_type/test'
    conn = setup_raw_submissions()
    conn.upload_file(file_path, Origin_Bucket_Name, key)
    event = {"Records": [{"Sns": {
        "Message": "{\"Records\":[{\"s3\":{\"bucket\":{\"name\":\"" + Origin_Bucket_Name + "\"}, \"object\":{\"key\":\"" + key + "\"}}}]}"}}]}
    lambda_function.lambda_handler(event, '')

@mock_s3
def test_auto_export():
    print('-----------------------TEST_AUTO_EXPORT--------------------------')
    run_auto_export('./tests/testFiles/test')
    assert True