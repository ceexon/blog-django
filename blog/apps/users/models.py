from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
import uuid
import jwt
from rest_framework_jwt.settings import api_settings
from ... import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

GENDER = (
    (1, 'Male'),
    (2, 'Female'),
    (3, 'Other'),
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_superuser=False, is_staff=True):
        if not email:
            raise ValueError('User must have an email address')
        if not password:
            raise ValueError('User must have a password')

        user_obj = self.model(
            email=self.normalize_email(email)
        )

        user_obj.set_password(password)
        user_obj.is_superuser = is_superuser
        user_obj.is_active = True
        user_obj.is_staff = is_staff
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
        )

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_superuser=True,
            is_staff=True,
        )

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=800, null=False, blank=False)
    active = models.BooleanField(default=True)  # can login
    is_superuser = models.BooleanField(default=False)  # superuser
    staff = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        return self.email

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email

    # @property
    # def is_active(self):
    #     return self.active

    # @property
    # def is_superuser(self):
    #     return self.admin

    # @property
    # def is_staff(self):
    #     return self.staff

    @property
    def gen_token(self):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(self)
        token = jwt_encode_handler(payload)

        return token


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=False, null=True)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    other_names = models.CharField(max_length=70, blank=False, null=False)
    gender = models.IntegerField(choices=GENDER)
    bio = models.TextField(max_length=500, blank=True)
    date_of_birth = models.DateTimeField(null=False, blank=False)
    GUID = models.UUIDField(default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.first_name+' '+self.other_names
