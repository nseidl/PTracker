from __future__ import unicode_literals

import logging
import logging.config
import json
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
CONFIG_LOCATION = os.path.join(__location__, 'logging_config.json')

DEFAULT_WARN_LIST = []


def get_logger(module=None, warn_list=[]):
    tag = 'PTracker' if module is None else module

    with open(CONFIG_LOCATION, 'r') as config_file:
        config_json = json.load(config_file)


    logging.config.dictConfig(config_json)

    warn_list = warn_list + DEFAULT_WARN_LIST
    [logging.getLogger(logger_name).setLevel(logging.WARNING) for logger_name in warn_list]

    new_logger = logging.getLogger(tag)

    return new_logger