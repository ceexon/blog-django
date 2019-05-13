from django.db import models
from django.utils import timezone
import uuid

GENDER = (
    (1, 'Male'),
    (2, 'Female'),
)


class User(models.Model):
    first_name = models.CharField(max_length=30, blank=False, null=False)
    other_names = models.CharField(max_length=70, blank=False, null=False)
    email = models.CharField(max_length=60)
    gender = models.IntegerField(choices=GENDER)
    year_of_birth = models.DateTimeField(null=False, blank=False)
    GUID = models.UUIDField(default=uuid.uuid4, editable=False)
    password = models.CharField(
        blank=False, null=False, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.first_name+' '+self.other_names
