import boto3
client = boto3.client('organizations')

# listing all AWS Organization's Accounts
#response = client.list_accounts()
# print(response)

# Create session using your current creds
boto_sts = boto3.client('sts')

# Request to assume the role like this, the ARN is the Role's ARN from
# the other account you wish to assume. Not your current ARN.
stsresponse = boto_sts.assume_role(
    RoleArn="OtherAccountARNGoesHere",
    RoleSessionName='newsession'
)

# Save the details from assumed role into vars
newsession_id = stsresponse["Credentials"]["AccessKeyId"]
newsession_key = stsresponse["Credentials"]["SecretAccessKey"]
newsession_token = stsresponse["Credentials"]["SessionToken"]

# Use the assumed session vars to create a new boto3 client with the assumed role creds
# Here I create an s3 client using the assumed creds.
s3_assumed_client = boto3.client(
    's3',
    region_name='us-east-1',
    aws_access_key_id=newsession_id,
    aws_secret_access_key=newsession_key,
    aws_session_token=newsession_token
)

# Here I create an s3 resource with the assumed creds
s3_assumed_resource = boto3.resource(
    's3',
    region_name='us-east-1',
    aws_access_key_id=newsession_id,
    aws_secret_access_key=newsession_key,
    aws_session_token=newsession_token
)

# Now we can use s3_assumed session for calls using the assumed role.
# As in this example where I list buckets using the assumed creds
response = s3_assumed_client.list_buckets()

# Or like this use of the resource to create a bucket object.
mybucket = s3_assumed_resource.Bucket('OtherAccountBucket')
