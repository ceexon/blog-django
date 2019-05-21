import cloudinary
from rest_framework.response import Response
from django.core.validators import URLValidator


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
