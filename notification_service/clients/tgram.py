import asyncio
import logging

import telegram
from notification_service.conf.settings import settings

logger = logging.getLogger(__name__)


class TelegramClient:

    def __init__(self):
        self.client = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)

    def send_sms(self, destination: str, message: str) -> None:
        asyncio.run(self.client.send_message(chat_id=destination, text=message))
