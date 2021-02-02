import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgres://rlpzzuuzbncnzp:46453c81fbe8f2b1d5a4baeda155237395b7399b8264b9895b107c04aaa7b58f@ec2-54-163-47-62.compute-1.amazonaws.com:5432/d1h7ptok5qvjmu'
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