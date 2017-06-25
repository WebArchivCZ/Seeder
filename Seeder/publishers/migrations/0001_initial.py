# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-25 16:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('last_changed', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phone', models.CharField(blank=True, max_length=128, null=True, verbose_name='Phone')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('position', models.CharField(blank=True, max_length=256, null=True, verbose_name='Position')),
            ],
            options={
                'verbose_name_plural': 'Publisher contacts',
                'verbose_name': 'Publisher contact',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('last_changed', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'Publishers',
                'verbose_name': 'Publisher',
            },
        ),
        migrations.AddField(
            model_name='contactperson',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='publishers.Publisher'),
        ),
    ]
