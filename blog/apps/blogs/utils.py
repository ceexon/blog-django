import cloudinary
from rest_framework.response import Response
from django.core.validators import URLValidator
from .models import Like
from django.shortcuts import get_object_or_404


def upload_image(image):
    """ Confirm image is of valid type """
    if not str(image.name).endswith(('.png', '.jpg', '.jpeg', '.gif')):
        return {"status": 400, "error": ["Ensure that the file is an image"]}

    image_data = cloudinary.uploader.upload(image)
    image_url = image_data['url']
    try:
        validate = URLValidator(
            schemes=('http', 'https', 'ftp', 'ftps', 'rtsp', 'rtmp'))
        validate(image_url)
    except ValidationError:
        return Response({
            "Error": "invalid image url",
        }, status=400)

    return {'status': "image found", "image": image_url}


def like_or_deslike(user, post, like):
    if like:
        liking = "Like"
    else:
        liking = "Dislike"

    post_like = Like.objects.filter(post=post, user=user)

    if not post_like:
        post_like = Like()
        post_like.user = user
        post_like.post = post

        if like:
            post_like.like = like
        else:
            post_like.like = False

        post_like.save()

    else:
        post_like = post_like[0]
        if post_like.like == like:
            return {
                "Forbidden": "You cannot {} twice".format(liking),
                "status": 403
            }

        else:
            post_like.like = like
            post_like.save()

    return {
        'post': post_like.post_id,
        'user': post_like.user_id,
        'Like': post_like.like,
        'action': liking,
        'status': 200
    }
