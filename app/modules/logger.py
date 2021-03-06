""" Global logging configuration. """

from logging.handlers import TimedRotatingFileHandler as tr_fh

from app import logger_dict as v

__author__ = "@ivanleoncz"

import logging

def config():
    """ Setting up log configuration. """

    conf = logging.getLogger(__name__)

    # avoids multiple log messages
    if not conf.handlers:
        conf.setLevel(logging.INFO)
        log_form = logging.Formatter('%(asctime)s [%(levelname)s]\t%(message)s')
        handler = None
        if LOG_ROTATE == True:
            # no log rotation will be performed, leaving to OS (logrotate)
            handler = logging.FileHandler(v.get("LOG_FILE"))
        elif LOG_ROTATE == False:
            # configuring log rotation (see pycaptive_settings.py)
            handler = tr_fh(v.get("LOG_FILE"),
                       when=v.get("LOG_ROTATE_WHEN"),
                backupCount=v.get("LOG_ROTATE_COUNT"))
        handler.setFormatter(log_form)
        conf.addHandler(handler)

    return conf
