import boto3

S3_client = boto3.client('s3')

# No location constraint needed for 'us-east-1'
response = S3_client.create_bucket(Bucket="bubdisha4999")
print(response)
