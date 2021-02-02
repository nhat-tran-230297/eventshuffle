import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False

    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    pass

class DebugConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True


config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig,
    'Testing': TestingConfig
}