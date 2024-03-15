from notification_service.sms.new_order import NewOrderSMS
from notification_service.sms.order_canceled import OrderCanceledSMS
from notification_service.sms.order_confirmed import OrderConfirmedSMS

sms_handlers = {
    NewOrderSMS.NAME: NewOrderSMS,
    OrderConfirmedSMS.NAME: OrderConfirmedSMS,
    OrderCanceledSMS.NAME: OrderCanceledSMS,
}
