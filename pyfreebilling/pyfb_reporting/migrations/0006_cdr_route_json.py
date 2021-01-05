# Generated by Django 2.1.9 on 2019-06-21 15:12

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyfb_reporting', '0005_remove_cdr_chan_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='cdr',
            name='route_json',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
            preserve_default=False,
        ),
    ]
