import boto3
import datetime
import logging
import pytz

# INTERVAL is the number of days to keep the EBS volumes
INTERVAL = 30

#Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_ebs(client):
    now = datetime.datetime.now(pytz.utc)
    start_time = now - datetime.timedelta(days=INTERVAL)
    try:
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

    except Exception as e:
        logging.error(f"Error fething volumes: {e}")


def delete_volumes(client, ebs_ids):
    try:
        if not ebs_ids:
            logging.info('No volumes to delete')
        elif len(ebs_ids) >= 1:
            confirmation = input('Are you sure you want to delete these volumes? [y/n]: ' + str(ebs_ids))
            if confirmation == 'y':
                for volume in ebs_ids:
                    logging.info('Deleted volumes: ' + str(volume))
                    client.delete_volume(VolumeId=volume)
            elif confirmation == 'n':
                logging.info('No volumes deleted')
            else:
                logging.info(f"Invalid input: {confirmation}")
    except Exception as e:
        logging.error(f"Error deleting volumes: {e}")


def main():
    client = boto3.client('ec2')
    ebs_ids = get_ebs(client)
    if get_ebs:
        delete_volumes(client, ebs_ids)
    else:
        logging.error("No volumes found")

if __name__ == "__main__":
    main()