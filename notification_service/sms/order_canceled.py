from notification_service.sms.base import SMSNotification
from notification_service.templates.sms import SMSTemplate


class OrderCanceledSMS(SMSNotification):
    NAME = SMSTemplate.ORDER_CANCELLED
    TEMPLATE = 'Ваше бронювання на {date_time} скасовано!'
