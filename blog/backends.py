import jwt
from . import settings
from .apps.users.models import User
from .apps.blogs.models import BlogPost


def decode_token(token):
    payload = jwt.decode(token, settings.SECRET_KEY)
    user = payload['user_id']

    return user


def is_owner(token, post_id):
    user_id = decode_token(token)
    post = BlogPost.objects.get(id=post_id)
    author = post.author.id

    if user_id == author:
        return True
    else:
        return False
