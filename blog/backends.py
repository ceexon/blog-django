import jwt
from . import settings
from .apps.users.models import User
from .apps.blogs.models import BlogPost
from django.shortcuts import get_object_or_404


def decode_token(request):
    try:
        token = request.auth.decode()
    except Exception:
        return {"status": 401, "message": "Token is missing"}

    payload = jwt.decode(token, settings.SECRET_KEY)
    user = payload['user_id']

    return {
        "status": 200,
        "user": user
    }


def is_owner(request, post_id):
    user_id = decode_token(request)
    post = get_object_or_404(BlogPost, id=post_id)
    author = post.author.id

    if user_id == author:
        return True
    else:
        return False
