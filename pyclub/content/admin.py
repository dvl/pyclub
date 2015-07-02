# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext as _
from django.utils.timezone import now

from . import forms, models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'status',
        'approved',
        'created_at',
        'approved_at',
        'created_by',
    )

    form = forms.PostForm

    actions = (
        'approve',
    )

    def approve(self, request, queryset):
        rows = (
            queryset.filter(
                status=models.Post.FINISHED,
                approved=False
            )
            .update(
                approved_at=now(),
                approved=True
            )
        )

        self.message_user(request, _('{0} posts approved'.format(rows)))
    approve.short_description = _('Approve selected posts')

    def save_model(self, request, obj, *args):
        if not obj.pk:
            obj.created_by = request.user
        obj.save()
