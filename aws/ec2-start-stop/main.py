import boto3
import logging
import sys

logging.basicConfig(level=logging.INFO, format='%(name)s :: %(levelname)s :: %(message)s')
logger = logging.getLogger(__name__)

def get_instances(client):
    try:
        instances = client.describe_instances()

        instances_ids = []

        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                instances_ids.append(instance['InstanceId'])

        return instances_ids

    except Exception as e:
        logger.error(f'Error fetching instances: {e}')


def get_instance_status(client):
    try:
        instances = client.describe_instances()

        instance_status = []

        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                instance_status.append(instance['State']['Name'])

        return instance_status

    except Exception as e:
        logger.error(f'Error fetching instance status: {e}')


def ec2_action(client, instances_ids, instance_status):
    try:
        action = sys.argv[1]
        if action == 'list':
            print('Instances available:')
            for instance_id, status in zip(instances_ids, instance_status):
                print(f'{instance_id} - {status}')

        else:
            confirmation = input(f'Are you sure you want to {action} these instances? {instances_ids} [y/n]: ')
            if confirmation == 'y':
                if action == 'start':
                    logger.info(f'Starting instances: {instances_ids}')
                    client.start_instances(InstanceIds=instances_ids)
                elif action == 'stop':
                    logger.info(f'Stopping instances: {instances_ids}')
                    client.stop_instances(InstanceIds=instances_ids)
                elif action == 'terminate':
                    logger.info(f'Terminating instances: {instances_ids}')
                    client.terminate_instances(InstanceIds=instances_ids)
                else:
                    logger.error(f'Invalid action: {action}')
            elif confirmation == 'n':
                logger.info(f'No instances to {action}')
            else:
                logger.error(f'Invalid input: {confirmation}')

    except Exception as e:
        logger.error(f'Unable to perform action, {e}')


def main():
    client = boto3.client('ec2')
    instances_ids = get_instances(client)
    instance_status = get_instance_status(client)
    if get_instances:
        ec2_action(client, instances_ids, instance_status)
    else:
        logger.error('No instances to perform actions')

if __name__ == '__main__':
    main()
