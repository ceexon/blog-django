import jwt
from . import settings
from .apps.users.models import User


def decode_token(token):
    payload = jwt.decode(token, settings.SECRET_KEY)
    user = payload['user_id']

    return user
