import random
import json
import base64
import boto3

def random_number1():
    return random.randint(0, 100)

def random_number2():
    return random.randint(0, 100)

def encode_base64(json_data):
    message = json.dumps(json_data).encode('utf-8')
    encoded_message = base64.b64encode(message).decode('utf-8')

    return encoded_message

def send_to_sqs():
    encoded_message = encode_base64(json_data)
    boto3.setup_default_session(region_name='us-east-1')
    sqs = boto3.client('sqs')
    queue_url = 'yor queue url'
    sqs.send_message(QueueUrl=queue_url, MessageBody=encoded_message)

json_data = {
    "a": random_number1(),
    "b": random_number2(),
}

if __name__ == "__main__":
    send_to_sqs()