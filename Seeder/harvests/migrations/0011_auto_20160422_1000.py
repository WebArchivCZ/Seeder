# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-22 10:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harvests', '0010_harvest_seeds_frozen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harvest',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
    ]