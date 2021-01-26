class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
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