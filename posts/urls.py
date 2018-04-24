from django.conf.urls import url
from .views import (
    post_list,
    post_create,
    post_delete,
    post_detail,
    post_update
)

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^create$', post_create, name='create'),
    url(r'^(?P<id>\d+)/delete/$', post_delete),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', post_update),
]
