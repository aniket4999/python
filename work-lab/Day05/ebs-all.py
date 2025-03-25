import  boto3

#def lambda_handler(event,context):

ec2_client = boto3.client('ec2',region_name='us-east-1')
    
snapshots = ec2_client.describe_snapshots (OwnerIds=['self'])['Snapshots']
snapshot_ids = [Snapshots['VolumeId'] for Snapshots in snapshots]

volumns = ec2_client.describe_volumes()['Volumes']
volume_ids = [volume['VolumeId'] for volume in volumns]


for snapshot_volume_id in snapshot_ids:
    if snapshot_volume_id in volume_ids:
        print(f"The match found with the snapshot volume: {snapshot_volume_id}")
    else:
        print(f"No match found for snapshot volume: {snapshot_volume_id}")

#print(snapshot_ids)

#print(volumns)

#print(volume_ids)