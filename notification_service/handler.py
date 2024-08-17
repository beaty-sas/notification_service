import logging
from typing import Any
from typing import Dict

from notification_service.clients import providers
from notification_service.schemas.sqs import SQSMessageSchema
from notification_service.sms import sms_handlers

logger = logging.getLogger(__name__)


def handle_message(msg: Dict[str, Any]) -> None:
    message = SQSMessageSchema(**msg)

    logger.info({'message': f'Start process {message.provider} message to {message.destination}'})

    provider = providers.get(message.provider)
    if not provider:
        logger.error({'message': f'Provider {message.provider} is not supported'})
        return

    sms_handler = sms_handlers.get(message.template)
    if not sms_handler:
        logger.error({'message': f'Template {message.template} is not supported'})
        return

    notificator = sms_handler(message.values, provider)
    notificator.process_sms(destination=message.destination)

    logger.info({'msg': f'Successfully process {message.provider} message to {message.destination}'})
