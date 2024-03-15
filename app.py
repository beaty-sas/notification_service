import logging.config

import ujson

from notification_service import __version__
from notification_service.conf.logger import LOG_CONFIG
from notification_service.handler import handle_message
from notification_service.sentry import init_sentry

logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger(__name__)


def lambda_handler(event, context):
    init_sentry()
    logger.info({'message': f'Started notification service. Version: {__version__}'})

    for record in event['Records']:
        try:
            handle_message(ujson.loads(record['body']))
        except Exception as err:
            logger.exception(err)
