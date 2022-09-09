# Program to find SNS Topics and Subscriptions
import boto3
import json

AWS_REGION = "ap-south-1"
sns = boto3.client('sns', region_name=AWS_REGION)

# Creating multiple SNS Topics
snsrange = range(1, 11)
dict_arn = {}
for a in snsrange:
    arn = sns.create_topic(Name=('Test_Topic_')+str(a))
    dict_arn[a] = arn
