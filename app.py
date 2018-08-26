import os

from server import constants
from server.custom_logging import get_logger
from server.public import create_app

logger = get_logger(module='PTracker App Runner')

config_name = os.environ.get('APP_SETTINGS')
app = create_app(config_name)

SETTINGS = {
    'host': constants.SERVER_DEFAULTS['HOST'],
    'port': constants.SERVER_DEFAULTS['PORT'],
}

# default is http://127.0.0.1:5000
if __name__ == '__main__':
    logger.info('running with {}'.format(SETTINGS))
    app.run(**SETTINGS)