import boto3
import sys

def get_running_instances():
    boto3.setup_default_session(region_name='us-east-1')
    ec2 = boto3.client('ec2')
    running_instances = ec2.describe_instances()

    instances_ids = []

    for reservation in running_instances['Reservations']:
        for instance in reservation['Instances']:
            instances_ids.append(instance['InstanceId'])

    return instances_ids

def ec2_action(instances_ids):
    boto3.setup_default_session(region_name='us-east-1')
    ec2 = boto3.client('ec2')
    action = sys.argv[1]

    if action == 'start':
        print('Starting instances: ' + str(instances_ids))
        ec2.start_instances(InstanceIds=instances_ids)
    elif action == 'stop':
        print('Stopping instances: ' + str(instances_ids))
        ec2.stop_instances(InstanceIds=instances_ids)
    elif action == 'terminate':
        print('Terminating instances: ' + str(instances_ids))
        ec2.terminate_instances(InstanceIds=instances_ids)
    else:
        print('Invalid action: ' + action)

if __name__ == "__main__":
    instances_ids = get_running_instances()
    ec2_action(instances_ids)