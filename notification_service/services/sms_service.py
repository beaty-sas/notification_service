import logging

from notification_service.schemas.sms import SMSPayloadSchema
from notification_service.sms import sms_handlers

logger = logging.getLogger(__name__)


def send_sms(sms_data: SMSPayloadSchema) -> None:
    logger.info({'message': f'Start process sms to {sms_data.phone_number}'})

    sms_handler = sms_handlers[sms_data.template]
    notificator = sms_handler(sms_data.values)
    notificator.process_sms(destination=sms_data.phone_number)

    logger.info({'msg': f'Successfully process sms to {sms_data.phone_number}'})
