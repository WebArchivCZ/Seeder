# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-05 00:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0010_auto_20160107_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='publishers.Publisher'),
        ),
        migrations.AlterField(
            model_name='emailnegotiation',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contracts.Contract'),
        ),
    ]