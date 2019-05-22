from . import views
from django.urls import path, include
from rest_framework.urls import url


urlpatterns = [
    path('new/', views.CreateBlogPost.as_view(), name='new-blog'),
    url(r'^(?P<id>[0-9]+)/$', views.RUDBlogPost.as_view(), name='user-detail'),
    url(r'^(?P<post_id>[0-9]+)/like/$',
        views.LikeBlogPost.as_view(), name='like-post'),
    url(r'^(?P<post_id>[0-9]+)/dislike/$',
        views.DislikeBlogPost.as_view(), name='dislike-post'),
    url(r'^(?P<post_id>[0-9]+)/likecount/$',
        views.CountBLogLikes.as_view(), name='dislike-post'),
    path('', views.ListBlogPosts.as_view(), name='all-blogs'),
]
