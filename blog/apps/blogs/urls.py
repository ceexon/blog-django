from .views import RUDBlogPost, ListBlogPosts, CreateBlogPost
from django.urls import path, include
from rest_framework.urls import url


urlpatterns = [
    path('new/', CreateBlogPost.as_view(), name='new-blog'),
    url(r'^(?P<id>[0-9]+)/$', RUDBlogPost.as_view(), name='user-detail'),
    path('', ListBlogPosts.as_view(), name='all-blogs'),
]
