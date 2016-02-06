# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-05 00:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='content_type_set_for_comment', to='contenttypes.ContentType', verbose_name='content type'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment_comments', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]