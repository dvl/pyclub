# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20150626_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='approved_at',
            field=model_utils.fields.MonitorField(blank=True, default=django.utils.timezone.now, verbose_name='Approved at', null=True, monitor='approved', when=set([True])),
        ),
    ]
