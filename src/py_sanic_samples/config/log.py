import logging


LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "default": {
            'format':'%(asctime)s %(filename)s %(lineno)s %(levelname)s %(message)s',
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "default",
        }
    },
    "disable_existing_loggers": True,
    "root": {
        "handlers": ["console"],
        "level": "DEBUG"
    },
}