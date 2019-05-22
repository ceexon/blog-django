from django.db import models
from ... import settings
from django.core.validators import URLValidator
from cloudinary.models import CloudinaryField

User = settings.AUTH_USER_MODEL


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    slug = models.SlugField(unique=True, max_length=200, blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.CharField(max_length=250, blank=True, null=True)
    image_url = models.CharField(max_length=250, blank=True, null=True)
    caption = models.CharField(max_length=150, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=None, blank=True, null=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, blank=True, null=True)
    like = models.BooleanField(blank=True, null=True, default=True)
