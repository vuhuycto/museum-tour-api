import logging


class BaseConfig:
    LOGGING_LEVEL = logging.INFO

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1/ar_museum_tour"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "secret"
