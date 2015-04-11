# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin

from .content.views import PostListView

urlpatterns = [
    url(r'', include('social.apps.django_app.urls', namespace='social')),

    url(r'', include('pyclub.content.urls', namespace='content')),

    url(r'^admin/', include(admin.site.urls)),
]
