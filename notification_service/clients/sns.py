import logging

import boto3

logger = logging.getLogger(__name__)


class AWSSNSClient:

    def __init__(self):
        self.client = boto3.client('sns')

    def send_sms(self, destination: str, message: str) -> None:
        self.client.publish(
            PhoneNumber=destination,
            Message=message
        )
        logger.info({
            'message': 'SNS sms notification has been sent to {}'.format(destination),
            'text': message,
        })
