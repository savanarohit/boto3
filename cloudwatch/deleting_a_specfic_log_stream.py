import boto3
import json

AWS_REGION = "ap-south-1"
client = boto3.client('logs', region_name=AWS_REGION)
retention_period_in_days = 5

# LogGroup Name
log_group_name = 'WebApp'

# Deleting a Specific LogStream from LogGroup
delete_response = client.delete_log_stream(
    logGroupName='WebApp',
    # It will only delete LogStream with a name of default
    logStreamName='default',
)
print("Specific Log Stream Deleted")
