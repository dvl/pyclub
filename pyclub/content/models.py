# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _

from autoslug import AutoSlugField

import bleach
import mistune
import mistune_hilite


class PostQuerySet(models.QuerySet):
    def finished(self):
        return self.filter(status=self.model.FINISHED)

    def draft(self):
        return self.filter(status=self.model.DRAFT)

    def approved(self):
        return self.filter(approved=True)

    def live(self):
        return self.finished().approved()


class Post(models.Model):
    DRAFT = 'draft'
    FINISHED = 'finished'

    STATUS_CHOICES = (
        (DRAFT, _('Draft')),
        (FINISHED, _('Finished')),
    )

    title = models.CharField(
        verbose_name=_('Title'),
        max_length=50,
    )

    body = models.TextField(
        verbose_name=_('Body'),
    )

    body_html = models.TextField(
        verbose_name='Body HTML',
    )

    slug = AutoSlugField(
        verbose_name=_('Slug'),
        populate_from='title',
    )

    status = models.CharField(
        verbose_name=_('Status'),
        max_length=9,
        choices=STATUS_CHOICES,
        default=DRAFT,
    )

    approved = models.BooleanField(
        verbose_name=_('Approved'),
        default=False,
    )

    approved_at = models.DateTimeField(
        verbose_name=_('Approved at'),
        blank=True,
        null=True,
        editable=False,
    )

    created_by = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
    )

    created_at = models.DateTimeField(
        verbose_name=_('Created at'),
        auto_now_add=True,
    )

    objects = PostQuerySet.as_manager()

    class Meta:
        get_latest_by = 'created_at'

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('post', args=(self.slug,))

    def save(self, *args, **kwargs):
        renderer = mistune_hilite.HiliteRenderer()
        md = mistune.Markdown(renderer=renderer)

        self.body_html = md(bleach.clean(self.body))

        super().save(*args, **kwargs)
