# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-07 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyfreebill', '0018_costsummary_salesummary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailaddress',
            name='location',
            field=models.CharField(choices=[(b'work', 'Work'), (b'home', 'Home'), (b'billing', 'Billing'), (b'cdr_month', 'CDR (Monthly)'), (b'cdr_week', 'CDR (Weekly)'), (b'cdr_day', 'CDR (Daily)'), (b'other', 'Other')], default=b'work', max_length=10, verbose_name='location'),
        ),
    ]