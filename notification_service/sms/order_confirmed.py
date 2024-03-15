from notification_service.sms.base import SMSNotification
from notification_service.templates.sms import SMSTemplate


class OrderConfirmedSMS(SMSNotification):
    NAME = SMSTemplate.ORDER_CONFIRMED
    TEMPLATE = 'Ваше бронювання на {date_time} підтверджено!'
