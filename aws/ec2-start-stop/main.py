import boto3
import logging
import sys

#Setup Logging
logging.basicConfig(level=logging.INFO)
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
        logging.error(f"Error fetching instances: {e}")


def ec2_action(client, instances_ids):
    try:
        action = sys.argv[1]
        confirmation = input('Are you sure you want to ' + action + ' these instances? [y/n]: \n' + str(instances_ids))

        if confirmation == 'y':
            if action == 'start':
                logging.info('Starting instances: ' + str(instances_ids))
                client.start_instances(InstanceIds=instances_ids)
            elif action == 'stop':
                logging.info('Stopping instances: ' + str(instances_ids))
                client.stop_instances(InstanceIds=instances_ids)
            elif action == 'terminate':
                logging.info('Terminating instances: ' + str(instances_ids))
                client.terminate_instances(InstanceIds=instances_ids)
            else:
                logging.info('Invalid action: ' + action)
        elif confirmation == 'n':
            logging.info('No instances to ' + action)
        else:
            logging.info(f"Invalid input: {confirmation}")
    
    except Exception as e:
        logging.error(f"Unable to perform action, {e}")


def main():
    client = boto3.client('ec2')
    instances_ids = get_instances(client)
    if get_instances:
        ec2_action(client, instances_ids)
    else:
        logging.error("No instances to perform actions")

if __name__ == "__main__":
    main()