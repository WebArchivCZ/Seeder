# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-08 16:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('source', '0019_delete_seedexport'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QualityAssuranceCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_changed', models.DateTimeField(auto_now=True)),
                ('content_changed', models.BooleanField(default=False, verbose_name='Content changed too much')),
                ('technical_quality_changed', models.BooleanField(default=False, verbose_name='Technical side decreased too much')),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
                ('source_action', models.CharField(choices=[(b'voting', 'Voting'), (b'duplicity', 'Duplicated record'), (b'waiting', 'Waiting for response'), (b'reevaluation', 'Waiting for reevaluation'), (b'technical', 'Technical review'), (b'communication', 'In communication'), (b'vote_accepted', 'Accepted by staff'), (b'vote_declined', 'Declined by staff'), (b'success', 'Archiving accepted'), (b'forced', 'Archiving without publisher consent'), (b'declined', 'Declined by publisher'), (b'ignored', 'Publisher ignored requests'), (b'expired', 'Contract expired'), (b'terminated', 'Contract terminated')], max_length=15, verbose_name='Resulting action')),
                ('checked_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Checked by')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='source.Source', verbose_name='Source')),
            ],
            options={
                'ordering': ('-last_changed',),
                'abstract': False,
            },
        ),
    ]
