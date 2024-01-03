import boto3
import logging
import sys

def get_running_instances():
    try:
        running_instances = ec2.describe_instances()

        instances_ids = []

        for reservation in running_instances['Reservations']:
            for instance in reservation['Instances']:
                instances_ids.append(instance['InstanceId'])

        return instances_ids

    except Exception as e:
        logging.error(f"Error fetching instances: {e}")
        return []

def ec2_action(instances_ids):
    try:
        action = sys.argv[1]
        confirmation = input('Are you sure you want to ' + action + ' these instances? [y/n]:' + str(instances_ids))

        if confirmation == 'y':
            if action == 'start':
                logging.info('Starting instances: ' + str(instances_ids))
                ec2.start_instances(InstanceIds=instances_ids)
            elif action == 'stop':
                logging.info('Stopping instances: ' + str(instances_ids))
                ec2.stop_instances(InstanceIds=instances_ids)
            elif action == 'terminate':
                logging.info('Terminating instances: ' + str(instances_ids))
                ec2.terminate_instances(InstanceIds=instances_ids)
            else:
                logging.info('Invalid action: ' + action)
        elif confirmation == 'n':
            logging.info('No instances to ' + action)
        else:
            logging.info(f"Invalid input: {confirmation}")
    
    except Exception as e:
        logging.error(f"Unable to perform action {e}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    ec2 = boto3.client('ec2')
    instances_ids = get_running_instances()
    ec2_action(instances_ids)
