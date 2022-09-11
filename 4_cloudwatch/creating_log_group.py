import boto3
import json

AWS_REGION = "ap-south-1"
client = boto3.client('logs', region_name=AWS_REGION)
retention_period_in_days = 5

# Creating a LogGroup
log_group_name = 'WebApp'
response = client.create_log_group(
    logGroupName=log_group_name,
    tags={
        'Type': 'Concept',
        'Frequency': '60 seconds',
        'Environment': 'Production',
        'RetentionPeriod': str(retention_period_in_days)
    }

)
