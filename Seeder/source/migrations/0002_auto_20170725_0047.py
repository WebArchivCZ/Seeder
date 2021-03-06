# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-25 00:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_cs',
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_cs',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name_en',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
