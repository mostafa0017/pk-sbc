# Generated by Django 2.1.8 on 2020-05-29 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyfb_reporting', '0010_auto_20200527_0725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cdr',
            name='billsec',
        ),
        migrations.RemoveField(
            model_name='cdr',
            name='cdr_acc',
        ),
    ]
