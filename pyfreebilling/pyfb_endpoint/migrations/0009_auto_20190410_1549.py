# Generated by Django 2.1.5 on 2019-04-10 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyfb_endpoint', '0008_auto_20190410_1547'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerendpoint',
            name='ppd',
        ),
        migrations.AddField(
            model_name='customerendpoint',
            name='ppi',
            field=models.BooleanField(default=False, help_text='put callerid in SIP P-Preferred-Id field if enabled', verbose_name='caller ID in PPD field'),
        ),
        migrations.AlterField(
            model_name='customerendpoint',
            name='pai',
            field=models.BooleanField(default=False, help_text='put callerid in SIP P-Asserted-Id field if enabled', verbose_name='caller ID in PAI field'),
        ),
        migrations.AlterField(
            model_name='providerendpoint',
            name='pai',
            field=models.BooleanField(default=False, help_text='put callerid in SIP P-Asserted-Id field if enabled', verbose_name='caller ID in PAI field'),
        ),
        migrations.AlterField(
            model_name='providerendpoint',
            name='ppi',
            field=models.BooleanField(default=False, help_text='put callerid in SIP P-Preferred-Id field if enabled', verbose_name='caller ID in PPD field'),
        ),
    ]
