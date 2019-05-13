from .views import CreateUser, RUDUser, ListUser, UserPosts
from django.urls import path, include
from rest_framework.urls import url


urlpatterns = [
    path('new/', CreateUser.as_view(), name='new-user'),
    url(r'^(?P<id>[0-9]+)/$', RUDUser.as_view(), name='user-detail'),
    path('', ListUser.as_view(), name='all-users'),
    # url(r'^posts/$', UserPosts.as_view(), name='user-posts'),h
    url(r'^posts/(?P<id>[0-9]+)/$', UserPosts.as_view(), name='user-posts'),
]
