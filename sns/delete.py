# Program to list all SNS Topics
import boto3
import json

AWS_REGION = "ap-south-1"
sns = boto3.client('sns', region_name=AWS_REGION)

# Deleting SNS Topic
response = sns.delete_topic(
    TopicArn='arn:aws:sns:ap-south-1:775861444406:Test1')
