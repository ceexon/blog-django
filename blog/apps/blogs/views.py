from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer


class CreateBlogPost(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class ListBlogPosts(generics.ListAPIView):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()


class RUDBlogPost(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()
