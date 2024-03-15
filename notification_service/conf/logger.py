from pythonjsonlogger import jsonlogger

from notification_service.conf.settings import settings


class BaseJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(BaseJsonFormatter, self).add_fields(log_record, record, message_dict)
        log_record['level'] = record.levelname
        log_record['logger'] = record.name


log_level = settings.LOG_LEVEL

LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'json': {
            '()': BaseJsonFormatter,
        },
        'local': {
            '()': 'logging.Formatter',
        },
    },
    'handlers': {
        'default': {
            'formatter': 'json',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {},
    'root': {'handlers': ['default'], 'level': log_level},
}
