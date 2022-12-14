import boto3
import json

AWS_REGION = "ap-south-1"
client = boto3.client('logs', region_name=AWS_REGION)
retention_period_in_days = 5

"""
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

"""

log_group_name = 'WebApp'

"""

log_stream_name = 'default'
response = client.create_log_stream(
    logGroupName=log_group_name,
    logStreamName=log_stream_name
)

log_stream_name = 'default2'
response = client.create_log_stream(
    logGroupName=log_group_name,
    logStreamName=log_stream_name
)

log_stream_name = 'default3'
response = client.create_log_stream(
    logGroupName=log_group_name,
    logStreamName=log_stream_name
)

# Deleting a Specific LogStream
delete_response = client.delete_log_stream(
    logGroupName='WebApp',
    logStreamName='default',
)
print("Log Stream Deleted")
"""

# Print all log_stream name
log_streams = client.describe_log_streams(
    logGroupName='WebApp',
    logStreamNamePrefix='default',
    limit=40
)
print(log_streams)

# delete_log_stream(log_group_name, log_stream_name, logs)
for stream in log_streams['logStreams']:
    log_stream_name = stream['logStreamName']
    print("Delete log stream:", log_stream_name)
    client.delete_log_stream(logGroupName=log_group_name,
                             logStreamName=log_stream_name)
