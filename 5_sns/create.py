# Program to create multiple SNS Topics
import boto3
import json

AWS_REGION = "ap-south-1"
sns = boto3.client('sns', region_name=AWS_REGION)

# Creating multiple SNS Topics
snsrange = range(1, 21)
for i in snsrange:
    arn = sns.create_topic(Name=('Test_Topic_')+str(i))
    print(arn)
