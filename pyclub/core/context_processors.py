# -*- coding: utf-8 -*-

from django.conf import settings


def site_settings(request):
    return {
        'SITE_NAME': settings.SITE_NAME,
        'TAG_LINE': settings.TAG_LINE,
    }
