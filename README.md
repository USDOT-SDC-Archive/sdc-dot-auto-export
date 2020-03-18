# sdc-dot-auto-export
Repository for the auto-export Lambda function

# Content of repository
This repository is the source control for the Lambda function for automatic export of data in team buckets. 

The main purpose of the lambda is to copy files from a team S3 bucket to another S3 bucket that is used for external access into the SDC.

## Unit Testing
The environment variables are located in the pytest.ini file. The pytest.ini file allows pytest to use environment variables in its execution. This requires an additional install of `pytest-env`.

# Production Release Notes
## Version 1.0 Release
### Description of New Features
This release contains the initial release of the auto-export Lambda function and some basic unit tests to reach 90% code coverage.

SDC-1399: Create Lambda for the auto-export process
SDC-1400: Send out emails from the lambda once auto-export occurrs
