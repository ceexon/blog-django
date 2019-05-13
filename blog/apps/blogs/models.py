from django.db import models
from ..users.models import User


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(default=None, blank=True, null=True)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return self.title

    def poster(self):
        poster = User.objects.get(id=self.user)
        return poster.first_name+' '+poster.other_names
