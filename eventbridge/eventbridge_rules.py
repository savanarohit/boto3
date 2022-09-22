import boto3
import json

AWS_REGION = "ap-south-1"
client = boto3.client('events', region_name=AWS_REGION)

# Print all EventBridge Rules using prefix
response = client.list_rules(
    NamePrefix='code',
    EventBusName='default',
    # NextToken='string',
    Limit=100
)

print(response)
