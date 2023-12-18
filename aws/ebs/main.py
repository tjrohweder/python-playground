import boto3
import datetime
import pytz

client = boto3.client('ec2')
interval = 30

def get_ebs():
    now = datetime.datetime.now(pytz.utc)
    start_time = now - datetime.timedelta(days=interval)

    ebs = client.describe_volumes(
        Filters=[
            {
                'Name': 'status',
                'Values': [
                    'available',
                ]
            }
        ]
    )

    ebs_ids = []

    for volume in ebs['Volumes']:
        if volume['CreateTime'].replace(tzinfo=pytz.utc) < start_time:
            ebs_ids.append(volume['VolumeId'])

    return ebs_ids

def delete_volumes(ebs_ids):
    for volume in ebs_ids:
        print('Deleting volumes: ' + str(volume))
        client.delete_volume(VolumeId=volume)
    if not ebs_ids:
        print('No volumes to delete')

if __name__ == "__main__":
    ebs_ids = get_ebs()
    delete_volumes(ebs_ids)
