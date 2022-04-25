import logging


class BaseConfig:
    LOGGING_LEVEL = logging.INFO

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1/ar_museum_tour"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "secret"

    BRAINTREE_MERCHANT_ID = "wgr3f2sckjzb6h8h"
    BRAINTREE_PUBLIC_KEY = "gdgmrnnhvfzxctrm"
    BRAINTREE_PRIVATE_KEY = "85dc9abc8b51959b295286c9acf3b186"
