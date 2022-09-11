import boto3
import json

AWS_REGION = "ap-south-1"
client = boto3.client('logs', region_name=AWS_REGION)
retention_period_in_days = 5

# Creating LogStream in LogGroup
log_group_name = 'WebApp'

# First Log Stream
log_stream_name = 'default'
response = client.create_log_stream(
    logGroupName=log_group_name,
    logStreamName=log_stream_name
)

# Second Log Stream
log_stream_name = 'default2'
response = client.create_log_stream(
    logGroupName=log_group_name,
    logStreamName=log_stream_name
)

# Third Log Stream
log_stream_name = 'default3'
response = client.create_log_stream(
    logGroupName=log_group_name,
    logStreamName=log_stream_name
)
