# -*- coding: utf-8 -*-

import uuid

from django.conf import settings
from django.db import models
from django.db.models import Max, F, Q
from django.utils.translation import ugettext as _


class PostQuerySet(models.QuerySet):
    def finished(self):
        return self.filter(status=self.model.FINISHED)

    def draft(self):
        return self.filter(status=self.model.DRAFT)

    def posts(self):
        return (
            self
            .annotate(
                last_created_at=Max('revision__created_at')
            )
            .filter(
                Q(revision__created_at=F('last_created_at')) &
                Q(revision__approved_author=True) &
                Q(revision__approved_staff=True)
            )
            .finished()
        )


class Post(models.Model):
    """ Deve se relacionar com a model :class:`Revision` para formar uma
    publicação, o correto é buscar sempre a ultima :class:`Revision`
    aprovada tanto pelo autor quanto pela staff """

    DRAFT = 'draft'
    FINISHED = 'finished'

    STATUS_CHOICES = (
        (DRAFT, _('Draft')),
        (FINISHED, _('Finished')),
    )

    status = models.CharField(
        verbose_name=_('Status'),
        max_length=9,
        choices=STATUS_CHOICES,
        default=DRAFT,
    )

    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
    )

    created_at = models.DateTimeField(
        verbose_name=_('Created at'),
        auto_now_add=True,
    )

    objects = PostQuerySet.as_manager()


class Revision(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

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
