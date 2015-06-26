# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about',
            field=models.TextField(max_length=90, blank=True, verbose_name='About you', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='bitbucket',
            field=models.CharField(max_length=90, blank=True, verbose_name='BitBucket username', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='facebook',
            field=models.CharField(max_length=90, blank=True, verbose_name='Facebook username', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='github',
            field=models.CharField(max_length=90, blank=True, verbose_name='GitHub username', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gitlab',
            field=models.CharField(max_length=90, blank=True, verbose_name='GitLab username', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gratipay',
            field=models.CharField(max_length=90, blank=True, verbose_name='Gratipay username', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='linkedin',
            field=models.CharField(max_length=90, blank=True, verbose_name='LinkedIn username', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='twitter',
            field=models.CharField(max_length=90, blank=True, verbose_name='Twitter username', null=True),
        ),
    ]
