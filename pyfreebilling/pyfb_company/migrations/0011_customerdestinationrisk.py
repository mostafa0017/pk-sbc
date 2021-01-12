# Generated by Django 2.2.17 on 2021-01-11 17:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pyfb_direction', '0004_auto_20200420_1605'),
        ('pyfb_company', '0010_auto_20201223_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDestinationRisk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyfb_company.Customer', verbose_name='customer')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyfb_direction.Region', verbose_name='riegion')),
                ('risk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pyfb_direction.Risk', verbose_name='risk')),
            ],
            options={
                'verbose_name': 'Customer Destination Risk',
                'verbose_name_plural': 'Customer Destination Risks',
                'db_table': 'pyfb_company_c_risk',
                'ordering': ('customer', 'region'),
                'unique_together': {('customer', 'region')},
            },
        ),
    ]
