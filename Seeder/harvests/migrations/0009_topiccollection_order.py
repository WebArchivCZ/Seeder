# Generated by Django 2.2 on 2019-06-07 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harvests', '0008_harvest_topic_collection_frequency'),
    ]

    operations = [
        migrations.AddField(
            model_name='topiccollection',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]
