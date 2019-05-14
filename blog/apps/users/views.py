from django.shortcuts import render
from rest_framework import generics, response, viewsets
from rest_framework.views import APIView
from .serializers import ProfileSerializer, LoginSerializer, UserSerializer
from ..blogs.models import BlogPost
from ..blogs.serializers import BlogPostSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import User, Profile


class CreateUser(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginUser(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        print('\n\n\n', request.data)
        serializer.is_valid(raise_exception=True)
        print('\n\n\n', serializer.data, '\n\n\n')

        return response.Response(serializer.data)


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
        posts = BlogPost.objects.filter(author=id)

        serializer = self.serializer_class(posts, many=True)
        return response.Response(serializer.data)
