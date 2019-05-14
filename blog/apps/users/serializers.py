from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User, Profile
from django.contrib.auth import authenticate


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'first_name', 'other_names',
                  'bio', 'gender', 'year_of_birth', 'user')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'profile')

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
        )

        profile_data = validated_data.pop('profile')
        profile = Profile.objects.create(
            user=user,
            first_name=profile_data['first_name'],
            other_names=profile_data['other_names'],
            gender=profile_data['gender'],
            bio=profile_data['bio'],
            year_of_birth=profile_data['year_of_birth'],
        )

        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.first_name = profile_data.get('first_name', profile.first_name)
        profile.other_names = profile_data.get(
            'other_names', profile.other_names)
        profile.gender = profile_data.get('gender', profile.gender)
        profile.bio = profile_data.get('bio', profile.bio)
        profile.year_of_birth = profile_data.get(
            'year_of_birth', profile.year_of_birth)
        profile.save()

        return instance


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'Email is required to log in'
            )

        if password is None:
            raise serializers.ValidationError(
                'Password is required to log in.'
            )

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'User with provided email and password was not found'
            )

        return {
            'id': user.id,
            'email': user.email,
            'token': user.gen_token,
            'message': 'Logged in successfully',
        }

    class Meta:
        model = User
        fields = ('email', 'password')
