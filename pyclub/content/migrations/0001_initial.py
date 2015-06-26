# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(verbose_name='Title', max_length=140)),
                ('body', models.TextField(verbose_name='Body')),
                ('body_html', models.TextField(verbose_name='Body HTML')),
                ('slug', models.SlugField(max_length=90, verbose_name='Slug')),
                ('status', models.CharField(max_length=9, verbose_name='Status', choices=[('draft', 'Draft'), ('finished', 'Finished')], default='draft')),
                ('approved', models.BooleanField(verbose_name='Approved', default=False)),
                ('created_at', models.DateTimeField(verbose_name='Created at', auto_now_add=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'created_at',
            },
        ),
    ]
