import datetime
import os

import jwt
from flask import request

from main import config
from main.commons.exceptions import Unauthorized


def generate_nonce():
    """
    Generate jti, it is a unique identified that is used to
    prevent the JWT from being replayed.
    """
    return os.urandom(4).hex()


def get_jwt_token():
    value = request.headers.get("Authorization", None)

    if not value or not value.startswith("Bearer ") or len(value.split(" ")) != 2:
        raise Unauthorized()

    return value.split(" ")[1]


def get_jwt_data(token: str):
    try:
        return jwt.decode(token, config.SECRET_KEY, algorithms=["HS256"])
    except jwt.DecodeError:
        return None


def verify_jwt_token(token: str):
    return get_jwt_data(token) is not None


def create_access_token(identity):
    return jwt.encode(
        {
            "iss": identity,
            "iat": datetime.datetime.now().timestamp(),
            "jti": generate_nonce(),
        },
        config.SECRET_KEY,
        algorithm="HS256",
    )
