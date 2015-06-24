# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'status',
        'created_at',
        'created_by',
    )
