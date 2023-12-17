# Start and Stop EC2 instances
This is a simple script to start and stop EC2 instances.

## Requirements
- AWS credentials
- Python 3.6+
- boto3

## Install dependencies
```bash
pip3 install -r requirements.txt
```

## Usage
```bash
python3 main.py [action] 
```
## Actions
- start
- stop
- terminate

## Configuration
To use this project you'll need to have exported your AWS credentials as environment variables:
```bash
export AWS_ACCESS_KEY_ID="anaccesskey"
export AWS_SECRET_ACCESS_KEY="asecretkey"
export AWS_DEFAULT_REGION="region"
```
