# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('body', models.TextField(verbose_name='Body')),
                ('body_html', models.TextField(verbose_name='Body HTML')),
                ('slug', autoslug.fields.AutoSlugField(populate_from='title', verbose_name='Slug', editable=False)),
                ('status', models.CharField(default='draft', max_length=9, verbose_name='Status', choices=[('draft', 'Draft'), ('finished', 'Finished')])),
                ('approved', models.BooleanField(default=False, verbose_name='Approved')),
                ('approved_at', models.DateTimeField(blank=True, null=True, verbose_name='Approved at', editable=False)),
                ('created_at', models.DateTimeField(verbose_name='Created at', auto_now_add=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'created_at',
            },
        ),
    ]
