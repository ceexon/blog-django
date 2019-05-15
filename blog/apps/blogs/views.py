from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import BlogPost
from ..users.models import User
from .serializers import BlogPostSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from blog.backends import decode_token


class CreateBlogPost(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = request.auth.decode()
        user_id = decode_token(token)
        user = User.objects.get(id=user_id)

        new_post = BlogPost()
        new_post.author = user
        new_post.title = serializer.data['title']
        new_post.content = serializer.data['content']
        new_post.save()

        response_data = {
            'title': serializer.data['title'],
            'content': serializer.data['content'],
            'author': user_id,
        }
        return Response(response_data, status=201)


class ListBlogPosts(generics.ListAPIView):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()


class RUDBlogPost(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()
