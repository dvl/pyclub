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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('status', models.CharField(max_length=9, default='draft', choices=[('draft', 'Draft'), ('finished', 'Finished')], verbose_name='Status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('body', models.TextField(verbose_name='Body')),
                ('approved_staff', models.BooleanField(default=False, verbose_name='Approved by staff')),
                ('approved_author', models.BooleanField(default=False, verbose_name='Approved by author')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(to='content.Post')),
            ],
        ),
    ]
