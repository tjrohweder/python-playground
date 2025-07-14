import boto3
import datetime
import logging
import pytz

INTERVAL = 30 #days

logging.basicConfig(level=logging.INFO, format='%(levelname)s :: %(message)s')
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
        logger.error(f'Error fething volumes: {e}')


def delete_volumes(client, ebs_ids):
    try:
        if not ebs_ids:
            logger.info('No volumes to delete')
        elif len(ebs_ids) >= 1:
            confirmation = input(f'Are you sure you want to delete these volumes? [y/n]: {ebs_ids}')
            if confirmation == 'y':
                for volume in ebs_ids:
                    logger.info(f'Deleted volumes: {volume}')
                    client.delete_volume(VolumeId=volume)
            elif confirmation == 'n':
                logger.info('No volumes deleted')
            else:
                logger.info(f'Invalid input: {confirmation}')
    except Exception as e:
        logger.error(f'Error deleting volumes: {e}')


def main():
    client = boto3.client('ec2')
    ebs_ids = get_ebs(client)
    if get_ebs:
        delete_volumes(client, ebs_ids)
    else:
        logger.error('No volumes found')

if __name__ == '__main__':
    main()
