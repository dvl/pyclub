# -*- coding: utf-8 -*-

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _

from . import choices


class Post(models.Model):
    """ Deve se relacionar com a model :class:`Revision` para formar uma
    publicação, o correto é buscar sempre a ultima :class:`Revision`
    aprovada tanto pelo autor quanto pela staff """
    status = models.CharField(
        verbose_name=_('Status'),
        max_length=9,
        choices=choices.STATUS,
        default=choices.DRAFT,
    )

    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
    )

    created_at = models.DateTimeField(
        verbose_name=_('Created at'),
        auto_now_add=True,
    )


class Revision(models.Model):
    post = models.ForeignKey(
        to=Post,
    )

    title = models.CharField(
        verbose_name=_('Title'),
        max_length=128,
    )

    body = models.TextField(
        verbose_name=_('Body'),
    )

    approved_staff = models.BooleanField(
        verbose_name=_('Approved by staff'),
        default=False,
    )

    approved_author = models.BooleanField(
        verbose_name=_('Approved by author'),
        default=False,
    )

    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
    )

    created_at = models.DateTimeField(
        verbose_name=_('Created at'),
        auto_now_add=True,
    )
