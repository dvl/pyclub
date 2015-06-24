# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    # url(r'^$', views.PostListView.as_view(), name='list'),
    url(r'^create/$', views.PostCreateView.as_view(), name='create'),
]
