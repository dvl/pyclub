# -*- coding: utf-8 -*-

from django.contrib import admin

from . import models


class RevisionInline(admin.TabularInline):
    model = models.Revision
    extra = 0


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (
        RevisionInline,
    )
