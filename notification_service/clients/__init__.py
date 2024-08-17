from notification_service.clients.bsg import BSGProvider
from notification_service.clients.sns import AWSSNSClient
from notification_service.clients.tgram import TelegramClient

providers = {
    'sns': AWSSNSClient,
    'bsg': BSGProvider,
    'telegram': TelegramClient,
}