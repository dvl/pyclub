# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='list'),
]
