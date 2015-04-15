# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


class RevisionInline(admin.StackedInline):
    model = models.Revision
    extra = 0


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'revision',
        'status',
        'created_at',
        'created_by',
    )

    inlines = (
        RevisionInline,
    )
