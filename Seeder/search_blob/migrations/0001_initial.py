# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-25 16:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('blob', models.TextField()),
                ('is_public', models.BooleanField(default=False)),
                ('record_id', models.PositiveIntegerField()),
                ('record_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='search_blob', to='contenttypes.ContentType')),
            ],
        ),
    ]
