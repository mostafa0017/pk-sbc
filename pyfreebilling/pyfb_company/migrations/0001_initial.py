# Generated by Django 2.1.4 on 2018-12-10 11:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_extensions.db.fields
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='company name - must be unique', max_length=200, unique=True, verbose_name='name')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name')),
                ('address', models.CharField(help_text='address', max_length=64, verbose_name='address')),
                ('contact_name', models.CharField(help_text='contact name', max_length=30, verbose_name='contact name')),
                ('contact_phone', models.CharField(help_text='contact phone number', max_length=30, verbose_name='contact phone')),
            ],
            options={
                'db_table': 'pyfb_company',
                'verbose_name': 'company',
                'ordering': ('name',),
                'verbose_name_plural': 'companies',
            },
        ),
        migrations.CreateModel(
            name='CompanyBalanceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('amount_debited', models.DecimalField(decimal_places=4, max_digits=12, verbose_name='amount debited')),
                ('amount_refund', models.DecimalField(decimal_places=4, max_digits=12, verbose_name='amount refund')),
                ('customer_balance', models.DecimalField(decimal_places=4, default=0, help_text='resulting customer balance.', max_digits=12, verbose_name='customer balance')),
                ('supplier_balance', models.DecimalField(decimal_places=4, default=0, help_text='resulting provider balance.', max_digits=12, verbose_name='provider balance')),
                ('operation_type', models.CharField(choices=[('customer', 'operation on customer account'), ('provider', 'operation on provider account')], default='customer', max_length=10, verbose_name='operation type')),
                ('external_desc', models.CharField(blank=True, max_length=255, verbose_name='public description')),
                ('internal_desc', models.CharField(blank=True, max_length=255, verbose_name='internal description')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companys', to='pyfb_company.Company', verbose_name='company')),
            ],
            options={
                'db_table': 'pyfb_company_balance_history',
                'verbose_name': 'company balance history',
                'ordering': ('company', '-created'),
                'verbose_name_plural': 'company balance history',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('account_number', models.TextField(max_length=100, verbose_name='account number')),
                ('credit_limit', models.DecimalField(decimal_places=4, default=0, help_text='Credit limit for postpaid account.', max_digits=12, verbose_name='credit limit')),
                ('low_credit_alert', models.DecimalField(decimal_places=4, default='10', help_text='Low credit limit alert.', max_digits=12, verbose_name='low credit level alert')),
                ('max_calls', models.PositiveIntegerField(default=1, help_text='maximum simultaneous calls allowed for this customer account.', verbose_name='max simultaneous calls')),
                ('calls_per_second', models.PositiveIntegerField(default=10, help_text='maximum calls per seconds allowed for this customer account.', verbose_name='max calls per second')),
                ('customer_enabled', models.BooleanField(default=True, verbose_name='customer enabled / disabled')),
                ('customer_balance', models.DecimalField(decimal_places=6, default=0, help_text='Actual customer balance.', max_digits=12, verbose_name='customer balance')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='pyfb_company.Company')),
            ],
            options={
                'db_table': 'pyfb_customer',
                'verbose_name': 'customer',
                'ordering': ('company',),
                'verbose_name_plural': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('supplier_enabled', models.BooleanField(default=True, verbose_name='provider enabled / disabled')),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='providers', to='pyfb_company.Company')),
            ],
            options={
                'db_table': 'pyfb_provider',
                'verbose_name': 'provider',
                'ordering': ('company',),
                'verbose_name_plural': 'providers',
            },
        ),
    ]