import boto3
from botocore.config import Config

my_config = Config(
    region_name='ap-south-1'
)
client = boto3.client('s3', config=my_config)

# Listing buckets in human readable format
all_buckets = client.list_buckets()
for bucket in all_buckets['Buckets']:
    bucket_name = bucket['Name']
    region = client.get_bucket_location(Bucket=bucket_name)[
        "LocationConstraint"]
    print(bucket_name, region)
