import logging

import sentry_sdk

from notification_service.conf.settings import settings

logger = logging.getLogger(__name__)


def init_sentry():
    try:
        sentry_sdk.init(dsn=settings.SENTRY_DSN, traces_sample_rate=1.0)
    except Exception as exc:
        logger.error(f'Sentry not configured. {exc}')
