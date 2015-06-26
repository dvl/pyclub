# -*- coding: utf-8 -*-

from django.contrib import admin

from . import forms, models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'status',
        'approved',
        'created_at',
        'created_by',
    )

    form = forms.PostForm

    def save_model(self, request, obj, *args):
        if not obj.pk:
            obj.created_by = request.user
        obj.save()
