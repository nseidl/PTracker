import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    TESTING = False


class ProductionConfig(Config):
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}