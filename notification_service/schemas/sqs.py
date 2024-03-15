from pydantic import BaseModel

from notification_service.schemas.sms import SMSPayloadSchema


class SQSMessageSchema(BaseModel):
    """Income SQS message schema"""

    send_sms: bool
    sms_data: SMSPayloadSchema | None = None
