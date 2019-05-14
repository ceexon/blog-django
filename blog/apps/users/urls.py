from .views import CreateUser, RUDUser, ListUser, UserPosts, LoginUser
from django.urls import path, include
from rest_framework.urls import url


urlpatterns = [
    path('new/', CreateUser.as_view(), name='new-user'),
    url(r'^(?P<id>[0-9]+)/$', RUDUser.as_view(), name='user-detail'),
    path('', ListUser.as_view(), name='all-users'),
    url(r'^login/?$', LoginUser.as_view()),
    url(r'^posts/(?P<id>[0-9]+)/$', UserPosts.as_view(), name='user-posts'),
]
