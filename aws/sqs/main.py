import random
import json
import base64
import logging
import boto3

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

QUEUE_URL = ''

def random_number1():
    return random.randint(0, 100)


def random_number2():
    return random.randint(0, 100)


def encode_base64(json_data):
    message = json.dumps(json_data).encode('utf-8')
    encoded_message = base64.b64encode(message).decode('utf-8')

    return encoded_message


def send_to_sqs(client, json_data):
    try:
        encoded_message = encode_base64(json_data)
        client.send_message(QueueUrl=QUEUE_URL, MessageBody=encoded_message)
        logger.info(f'Message sent to SQS: {json_data}')

    except Exception as e:
        logger.error(f'Erorr sending message to SQS: {e}')

json_data = {
    'a': random_number1(),
    'b': random_number2(),
}

def main():
    client = boto3.client('sqs')
    send_to_sqs(client, json_data)

if __name__ == '__main__':
    main()
