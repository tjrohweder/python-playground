# Delete old EBS Volumes
Simple script to delete old EBS Volumes.

## Requirements
- AWS credentials
- Python 3.6+
- boto3
- pytz

## Configuration
To use this project you'll need to have exported your AWS credentials as environment variables:
```bash
export AWS_ACCESS_KEY_ID="anaccesskey"
export AWS_SECRET_ACCESS_KEY="asecretkey"
export AWS_DEFAULT_REGION="region"
```

## Install dependencies
```bash
pip install -r requirements.txt
```

## Variables
- interval: Interval in days to delete old EBS Volumes

## Usage
```bash
python main.py
```
