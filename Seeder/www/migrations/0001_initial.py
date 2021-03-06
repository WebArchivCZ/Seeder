# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-25 16:49
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('source', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('last_changed', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('title_cs', models.CharField(max_length=150, null=True)),
                ('title_en', models.CharField(max_length=150, null=True)),
                ('annotation', ckeditor.fields.RichTextField()),
                ('annotation_cs', ckeditor.fields.RichTextField(null=True)),
                ('annotation_en', ckeditor.fields.RichTextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('annotation_source_1', ckeditor.fields.RichTextField(blank=True, help_text='Leave empty to use source annotation', null=True, verbose_name='annotation for first source')),
                ('annotation_source_1_cs', ckeditor.fields.RichTextField(blank=True, help_text='Leave empty to use source annotation', null=True, verbose_name='annotation for first source')),
                ('annotation_source_1_en', ckeditor.fields.RichTextField(blank=True, help_text='Leave empty to use source annotation', null=True, verbose_name='annotation for first source')),
                ('annotation_source_2', ckeditor.fields.RichTextField(blank=True, help_text='Leave empty to use source annotation', null=True, verbose_name='annotation for second source')),
                ('annotation_source_2_cs', ckeditor.fields.RichTextField(blank=True, help_text='Leave empty to use source annotation', null=True, verbose_name='annotation for second source')),
                ('annotation_source_2_en', ckeditor.fields.RichTextField(blank=True, help_text='Leave empty to use source annotation', null=True, verbose_name='annotation for second source')),
                ('source_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='news_a', to='source.Source', verbose_name='First source')),
                ('source_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='news_b', to='source.Source', verbose_name='second source')),
            ],
            options={
                'verbose_name_plural': 'News articles',
                'verbose_name': 'News article',
            },
        ),
        migrations.CreateModel(
            name='Nomination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('last_changed', models.DateTimeField(auto_now=True)),
                ('url', models.CharField(max_length=256, verbose_name='URL')),
                ('contact_email', models.EmailField(max_length=254, verbose_name='Contact email')),
                ('name', models.CharField(blank=True, max_length=64, verbose_name='Name')),
                ('submitted_by_author', models.BooleanField(default=False)),
                ('is_cc', models.BooleanField(default=False, verbose_name='Licensed under creative commons')),
                ('note', models.CharField(blank=True, max_length=128, verbose_name='Note')),
                ('resolved', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('created',),
                'verbose_name_plural': 'Nominations',
                'verbose_name': 'Nomination',
            },
        ),
        migrations.CreateModel(
            name='SearchLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_term', models.CharField(max_length=256)),
                ('log_time', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('ip_address', models.GenericIPAddressField()),
            ],
        ),
    ]
