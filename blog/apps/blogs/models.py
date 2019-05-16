from django.db import models
from ... import settings
from django.core.validators import URLValidator

User = settings.AUTH_USER_MODEL


class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.TextField(max_length=1000, validators=[
                             URLValidator], null=True, blank=True)
    caption = models.CharField(max_length=150, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=None, blank=True, null=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return self.title
