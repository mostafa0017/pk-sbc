# Generated by Django 2.1.4 on 2019-05-20 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyfb_rating', '0004_auto_20181221_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerrcallocation',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyfb_company.Customer', verbose_name='customer'),
        ),
        migrations.AlterField(
            model_name='customerrcallocation',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, help_text='ratecard discount. For 10% discount, enter 10 !', max_digits=5, verbose_name='discount'),
        ),
        migrations.AlterField(
            model_name='customerrcallocation',
            name='tech_prefix',
            field=models.CharField(blank=True, default='', max_length=7, verbose_name='technical prefix'),
        ),
    ]