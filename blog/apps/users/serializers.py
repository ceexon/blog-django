from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'other_names',
            'year_of_birth',
            'email',
            'gender',
            'created_at',
        ]
        # fields = '__all__'
