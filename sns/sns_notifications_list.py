# Program to find SNS Topics and Subscriptions
import boto3
import json

AWS_REGION = "ap-south-1"
sns = boto3.client('sns', region_name=AWS_REGION)


# Function for creating sns topics
def snscreate():
    resposne = sns.create_topic(Name='Test3')


# Creating multiple SNS Topics
snscreate()


"""
# List SNS Topics
response = sns.list_topics()
for each_sns in response['Topics']:
    print(each_sns['TopicArn'])

# List SNS Topics with Subscriptions ARN
response = sns.list_subscriptions()
for each_subs in response['Subscriptions']:
    print(each_subs['SubscriptionArn'])
"""
