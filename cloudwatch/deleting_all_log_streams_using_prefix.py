import boto3
import json

AWS_REGION = "ap-south-1"
client = boto3.client('logs', region_name=AWS_REGION)
retention_period_in_days = 5

log_group_name = 'WebApp'

# Print all LogStream names using prefix
log_streams = client.describe_log_streams(
    logGroupName='WebApp',
    # This is prefix example, So Log stream will start with default keyword like default1, default2 , default3 .....
    logStreamNamePrefix='default',
    limit=40
)
print(log_streams)

# Deleting all LogStream using prefix
for stream in log_streams['logStreams']:
    log_stream_name = stream['logStreamName']
    print("Deleted log stream:", log_stream_name)
    client.delete_log_stream(logGroupName=log_group_name,
                             logStreamName=log_stream_name)
