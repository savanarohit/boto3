# Program for listing EventBridge rules with a specific name
from multiprocessing.sharedctypes import Value
from unittest import result
import boto3
import re
import json
import dictpy

# AWS Region details
AWS_REGION = "ap-south-1"
client = boto3.client('events', region_name=AWS_REGION)

# List all Event Bridge rules
response = client.list_rules()
# print(type(response))
# print(response)

string_obj = json.dumps(response)
# print(type(string_obj))
# print(string_obj)
search = re.search("demo", string_obj)
print(search)


"""
search = dictpy.DictSearch(data=response, target={"Name": "[demo]"})
print(search.result)


search = {"Rules": "codepipeline-demo-main-857365-rule"}
for key, value in response.items():
    if key == search:
        print(key)
    break


# get only specific key:values from json
for rules in response['Rules']:
   print(rules['Name'], rules['Arn'], rules['State'])

find = 'codepipeline-demo-main-857365-rule'

if find in response:
    print(find)
else:
    print('Not Found')

# Transform json input to python objects
dict = json.loads(response)

# Filter python objects with list comprehensions
result = [obj for obj in dict if (obj['Name'] == 'demo')]

"""
