# Generated by Django 2.1.4 on 2018-12-21 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyfb_did', '0002_auto_20181221_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='did',
            name='description',
            field=models.CharField(blank=True, max_length=30, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='routesdid',
            name='description',
            field=models.CharField(blank=True, max_length=30, verbose_name='description'),
        ),
    ]