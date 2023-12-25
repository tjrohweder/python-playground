import random
import json
import base64
import logging
import boto3

queue_url = 'https://sqs.us-east-1.amazonaws.com/250566739804/test'

def random_number1():
    return random.randint(0, 100)

def random_number2():
    return random.randint(0, 100)

def encode_base64(json_data):
    message = json.dumps(json_data).encode('utf-8')
    encoded_message = base64.b64encode(message).decode('utf-8')

    return encoded_message

def send_to_sqs():
    try:
        encoded_message = encode_base64(json_data)
        sqs.send_message(QueueUrl=queue_url, MessageBody=encoded_message)
        logging.info(f"Message sent to SQS: {json_data}")
    except Exception as e:
        logging.error(f"Erorr sending message to SQS: {e}")

json_data = {
    "a": random_number1(),
    "b": random_number2(),
}

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    sqs = boto3.client('sqs')
    send_to_sqs()