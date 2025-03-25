import boto3

# Create an EC2 client
client = boto3.client('ec2', region_name='us-east-1')

# Describe all EC2 volumes
response = client.describe_volumes()

# Extract the volumes information
volumes = response['Volumes']

# Print the volumes information
print(volumes)
