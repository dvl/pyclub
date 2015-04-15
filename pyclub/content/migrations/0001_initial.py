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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('finished', 'Finished')], max_length=9, verbose_name='Status', default='draft')),
                ('created_at', models.DateTimeField(verbose_name='Created at', auto_now_add=True)),
            ],
            options={
                'get_latest_by': 'created_at',
            },
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name='Title')),
                ('body', models.TextField(verbose_name='Body')),
                ('approved_staff', models.BooleanField(verbose_name='Approved by staff', default=False)),
                ('approved_author', models.BooleanField(verbose_name='Approved by author', default=False)),
                ('created_at', models.DateTimeField(verbose_name='Created at', auto_now_add=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(to='content.Post')),
            ],
            options={
                'get_latest_by': 'created_at',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='active_revision',
            field=models.ForeignKey(related_name='active_revision', to='content.Revision'),
        ),
        migrations.AddField(
            model_name='post',
            name='created_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
