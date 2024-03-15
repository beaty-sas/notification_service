from typing import Any
from typing import Dict

from notification_service.schemas.sqs import SQSMessageSchema
from notification_service.services.sms_service import send_sms


def handle_message(msg: Dict[str, Any]) -> None:
    sqs_message = SQSMessageSchema(**msg)

    if sqs_message.send_sms and sqs_message.sms_data:
        send_sms(sqs_message.sms_data)
