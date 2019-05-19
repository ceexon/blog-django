import jwt
from . import settings
from .apps.users.models import User
from .apps.blogs.models import BlogPost
from django.shortcuts import get_object_or_404


def decode_token(token):
    payload = jwt.decode(token, settings.SECRET_KEY)
    user = payload['user_id']

    return user


def is_owner(token, post_id):
    user_id = decode_token(token)
    post = get_object_or_404(BlogPost, id=post_id)
    author = post.author.id

    if user_id == author:
        return True
    else:
        return False
