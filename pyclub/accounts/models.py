# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext as _


class User(AbstractUser):
    about = models.TextField(
        verbose_name=_('About you'),
        max_length=90,
        blank=True,
        null=True,
    )

    github = models.CharField(
        verbose_name=_('GitHub username'),
        max_length=90,
        blank=True,
        null=True,
    )

    bitbucket = models.CharField(
        verbose_name=_('BitBucket username'),
        max_length=90,
        blank=True,
        null=True,
    )

    gitlab = models.CharField(
        verbose_name=_('GitLab username'),
        max_length=90,
        blank=True,
        null=True,
    )

    twitter = models.CharField(
        verbose_name=_('Twitter username'),
        max_length=90,
        blank=True,
        null=True,
    )

    facebook = models.CharField(
        verbose_name=_('Facebook username'),
        max_length=90,
        blank=True,
        null=True,
    )

    linkedin = models.CharField(
        verbose_name=_('LinkedIn username'),
        max_length=90,
        blank=True,
        null=True,
    )

    gratipay = models.CharField(
        verbose_name=_('Gratipay username'),
        max_length=90,
        blank=True,
        null=True,
    )

    def display_name(self):
        if not self.get_full_name():
            return getattr(self, self.USERNAME_FIELD)

        return self.get_full_name()
