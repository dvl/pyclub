# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^dashboard/', include('pyclub.dashboard.urls', namespace='dashboard')),
    url(r'^content/', include('pyclub.content.urls', namespace='content')),
    url(r'', include('django.contrib.auth.urls')),
    url(r'', include('social.apps.django_app.urls', namespace='social')),

    url(r'^admin/', include(admin.site.urls)),
]
