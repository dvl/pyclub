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

    def approved_posts(self):
        """ Filtra somente os posts que possuem revisões aprovadas """
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

    active_revision = models.ForeignKey(
        to='Revision',
        related_name='active_revision'
    )

    objects = PostQuerySet.as_manager()

    class Meta:
        get_latest_by = 'created_at'

    def __str__(self):
        return '{}'.format(self.pk)

    def get_last_approved_revision(self):
        return self.revision_set.approved().latest()


class RevisionQuerySet(models.QuerySet):
    def staff_approved(self):
        return self.filter(approved_staff=True)

    def author_approved(self):
        return self.filter(approved_author=True)

    def approved(self):
        return self.staff_approved().author_approved()


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

    objects = RevisionQuerySet.as_manager()

    class Meta:
        get_latest_by = 'created_at'

    def __str__(self):
        return '{}'.format(self.pk)
