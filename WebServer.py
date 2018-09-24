#!/usr/bin/env python
import os
import sys
import ConfigureUtil
import logging.config

logging.config.fileConfig('log.conf')
logger = logging.getLogger('WebServer')

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    if(len(sys.argv) == 1):
        args=[sys.argv[0], "runserver", "0.0.0.0:8000"];
    ConfigureUtil.load_notice()
    try:
        execute_from_command_line(args)
    except Exception as e:
        logger.error("WebServer crash %s", e)
