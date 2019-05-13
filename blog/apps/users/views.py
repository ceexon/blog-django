from django.shortcuts import render
from rest_framework import generics, response
from .serializers import UserSerializer
from ..blogs.models import BlogPost
from ..blogs.serializers import BlogPostSerializer
from .models import User


class CreateUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RUDUser(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserPosts(generics.ListAPIView):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()
    lookup_field = "id"

    def list(self, request, id, *args, **kwargs):
        posts = BlogPost.objects.filter(user=id)

        serializer = self.serializer_class(posts, many=True)
        return response.Response(serializer.data)
