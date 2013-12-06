from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from jsonview.decorators import json_view
from app import views


urlpatterns = patterns(
    '',
    url(r'^wishlist/?(?P<id>\d+)?$',
        login_required(json_view(views.Wishlist.as_view())),
        name='wishlist'),
    url(r'^giftees/?(?P<id>\d+)?$',
        login_required(json_view(views.Giftees.as_view())),
        name='giftees'),
    url(r'^shopping/?(?P<id>\d+)?$',
        login_required(json_view(views.Shopping.as_view())),
        name='shopping'),
    url(r'^users/?$',
        login_required(json_view(views.Users.as_view())),
        name='users')
)
