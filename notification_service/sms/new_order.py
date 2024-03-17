from notification_service.sms.base import SMSNotification
from notification_service.templates.sms import SMSTemplate


class NewOrderSMS(SMSNotification):
    NAME = SMSTemplate.NEW_ORDER
    TEMPLATE = 'Нове бронювання від {name} на {date_time}'
