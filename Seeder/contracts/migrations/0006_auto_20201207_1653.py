# Generated by Django 2.2.13 on 2020-12-07 16:53

import contracts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0005_remove_contract_creative_commons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='year',
            field=models.PositiveIntegerField(default=contracts.models.this_year, verbose_name='Year'),
        ),
    ]
