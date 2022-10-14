# Program for listing EventBridge rules with a specific name
import boto3
# from boto3.session import Session
import re
import json

# AWS Region details
AWS_REGION = "ap-south-1"
client = boto3.client('events', region_name=AWS_REGION)

# List all Event Bridge rules
response = client.list_rules()
# print(type(response))
# print(response)

for r in response['Rules']:
    rule = r['Name']
    arn = r['Arn']
    state = r['State']
    bus = r['EventBusName']
    print(rule, arn, state)


string_obj = json.dumps(response)
# print(type(string_obj))
# print(string_obj)
search = re.search("demo", string_obj)
print(search)


# listing all regions using session
#s = Session()
#ec2_regions = s.get_available_regions('ec2')
# print(ec2_regions)
