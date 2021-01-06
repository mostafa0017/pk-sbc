# Generated by Django 2.1.8 on 2019-05-21 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pyfb_routing', '0002_auto_20181221_1409'),
        ('pyfb_kamailio', '0007_auto_20190306_1514'),
        ('pyfb_endpoint', '0009_auto_20190410_1549'),
        ('pyfb_direction', '0003_auto_20190327_1733'),
        ('pyfb_company', '0004_auto_20181210_1138'),
        ('pyfb_rating', '0005_auto_20190520_1604'),
        ('pyfb_reporting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CDR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_ip', models.CharField(help_text='Customer IP address.', max_length=100, null=True, verbose_name='customer IP address')),
                ('aleg_uuid', models.CharField(max_length=100, null=True, verbose_name='a leg call-ID')),
                ('bleg_uuid', models.CharField(default='', max_length=100, null=True, verbose_name='b leg call-ID')),
                ('rtp_uuid', models.CharField(max_length=100, null=True, verbose_name='media call-ID')),
                ('caller_number', models.CharField(max_length=100, null=True, verbose_name='caller ID num')),
                ('callee_number', models.CharField(max_length=100, null=True, verbose_name='Dest. number')),
                ('chan_name', models.CharField(max_length=100, null=True, verbose_name='channel name')),
                ('start_stamp', models.DateTimeField(db_index=True, null=True, verbose_name='start time')),
                ('answered_stamp', models.DateTimeField(null=True, verbose_name='answered time')),
                ('end_stamp', models.DateTimeField(null=True, verbose_name='hangup time')),
                ('duration', models.IntegerField(null=True, verbose_name='global duration')),
                ('effectiv_duration', models.IntegerField(help_text='Global call duration since call has been received by the switch in ms.', null=True, verbose_name='total duration')),
                ('effective_duration', models.IntegerField(help_text='real call duration in s.', null=True, verbose_name='effective duration')),
                ('billsec', models.IntegerField(help_text='billed call duration in s.', null=True, verbose_name='billed duration')),
                ('read_codec', models.CharField(max_length=20, null=True, verbose_name='read codec')),
                ('write_codec', models.CharField(max_length=20, null=True, verbose_name='write codec')),
                ('sip_code', models.CharField(db_index=True, max_length=3, null=True, verbose_name='hangup SIP code')),
                ('sip_reason', models.TextField(max_length=255, null=True, verbose_name='hangup SIP reason')),
                ('cost_rate', models.DecimalField(decimal_places=5, default='0', max_digits=11, null=True, verbose_name='buy rate')),
                ('total_sell', models.DecimalField(decimal_places=5, default='0', max_digits=11, null=True, verbose_name='total sell')),
                ('total_cost', models.DecimalField(decimal_places=5, default='0', max_digits=11, null=True, verbose_name='total cost')),
                ('rate', models.DecimalField(decimal_places=5, max_digits=11, null=True, verbose_name='sell rate')),
                ('init_block', models.DecimalField(decimal_places=5, max_digits=11, null=True, verbose_name='Connection fee')),
                ('block_min_duration', models.IntegerField(null=True, verbose_name='increment')),
                ('sip_charge_info', models.CharField(help_text='Contents of the P-Charge-Info header for billing purpose.', max_length=100, null=True, verbose_name='charge info')),
                ('sip_user_agent', models.CharField(max_length=100, null=True, verbose_name='sip user agent')),
                ('sip_rtp_rxstat', models.CharField(max_length=30, null=True, verbose_name='sip rtp rx stat')),
                ('sip_rtp_txstat', models.CharField(max_length=30, null=True, verbose_name='sip rtp tx stat')),
                ('kamailio_server', models.IntegerField(default=1, verbose_name='SIP server')),
                ('hangup_disposition', models.CharField(default='', max_length=100, null=True, verbose_name='hangup disposition')),
                ('sip_hangup_cause', models.CharField(default='', max_length=100, null=True, verbose_name='SIP hangup cause')),
                ('direction', models.CharField(blank=True, help_text='Type of calls.', max_length=10, null=True, verbose_name='Type of call')),
                ('callee_destintaion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cdrs_2', to='pyfb_direction.Destination', verbose_name='calle destination')),
                ('caller_destination', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cdrs', to='pyfb_direction.Destination', verbose_name='caller destination')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_related', to='pyfb_company.Customer', verbose_name='customer')),
                ('customer_endpoint', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cdrs', to='pyfb_endpoint.CustomerEndpoint', verbose_name='customer endpoint')),
                ('lcr_carrier_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='carrier_related', to='pyfb_company.Provider', verbose_name='provider')),
                ('lcr_group_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cdrs', to='pyfb_routing.RoutingGroup', verbose_name='routing group')),
                ('media_server', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cdrs', to='pyfb_kamailio.RtpEngine', verbose_name='Media server name')),
                ('provider_endpoint', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cdrs', to='pyfb_endpoint.ProviderEndpoint', verbose_name='provider endpoint')),
                ('ratecard_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cdrs', to='pyfb_rating.CustomerRatecard', verbose_name='ratecard')),
            ],
            options={
                'verbose_name': 'cdr',
                'verbose_name_plural': 'cdrs',
                'db_table': 'pyfb_reporting_cdr',
                'ordering': ('-start_stamp',),
            },
        ),
        migrations.CreateModel(
            name='DimCustomerDestination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_calls', models.IntegerField(default=0, verbose_name='total calls')),
                ('success_calls', models.IntegerField(default=0, verbose_name='success calls')),
                ('total_duration', models.IntegerField(default=0, verbose_name='total duration')),
                ('avg_duration', models.IntegerField(default=0, verbose_name='average duration')),
                ('max_duration', models.IntegerField(default=0, verbose_name='max duration')),
                ('min_duration', models.IntegerField(default=0, verbose_name='min duration')),
                ('total_sell', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='total sell')),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='total cost')),
                ('direction', models.CharField(choices=[('pstn', 'Outbound calls'), ('did', 'DID - Inbound calls'), ('pstn2did', 'Outbound calls to internal DID'), ('emergency', 'Emergency calls')], default='pstn', help_text='Type of calls.', max_length=10, verbose_name='Type of call')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dimcustomerdestinations', to='pyfb_company.Customer', verbose_name='customer')),
            ],
            options={
                'db_table': 'pyfb_reporting_dim_cust_dest',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='DimCustomerHangupcause',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hangupcause', models.CharField(blank=True, max_length=100, null=True, verbose_name='hangupcause')),
                ('total_calls', models.IntegerField(verbose_name='total calls')),
                ('direction', models.CharField(help_text='Type of calls.', max_length=10, verbose_name='Type of call')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dimcustomerhangupcauses', to='pyfb_company.Customer', verbose_name='customer')),
            ],
            options={
                'db_table': 'pyfb_reporting_dim_cust_hc',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='DimCustomerSipHangupcause',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sip_hangupcause', models.CharField(blank=True, max_length=100, null=True, verbose_name='sip hangupcause')),
                ('total_calls', models.IntegerField(verbose_name='total calls')),
                ('direction', models.CharField(choices=[('pstn', 'Outbound calls'), ('did', 'DID - Inbound calls'), ('pstn2did', 'Outbound calls to internal DID'), ('emergency', 'Emergency calls')], default='pstn', help_text='Type of calls.', max_length=10, verbose_name='Type of call')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dimcustomersiphangupcauses', to='pyfb_company.Customer', verbose_name='customer')),
            ],
            options={
                'db_table': 'pyfb_reporting_dim_cust_sip_hc',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='DimDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('day', models.CharField(max_length=2, verbose_name='day')),
                ('day_of_week', models.CharField(max_length=30, verbose_name='day of the week')),
                ('hour', models.CharField(blank=True, max_length=2, null=True, verbose_name='hour')),
                ('month', models.CharField(max_length=2, verbose_name='month')),
                ('quarter', models.CharField(max_length=2, verbose_name='quarter')),
                ('year', models.CharField(max_length=4, verbose_name='year')),
            ],
            options={
                'db_table': 'pyfb_reporting_dim_date',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='DimProviderDestination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_calls', models.IntegerField(default=0, verbose_name='total calls')),
                ('success_calls', models.IntegerField(default=0, verbose_name='success calls')),
                ('total_duration', models.IntegerField(default=0, verbose_name='total duration')),
                ('avg_duration', models.IntegerField(default=0, verbose_name='average duration')),
                ('max_duration', models.IntegerField(default=0, verbose_name='max duration')),
                ('min_duration', models.IntegerField(default=0, verbose_name='min duration')),
                ('total_sell', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='total sell')),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='total cost')),
                ('direction', models.CharField(choices=[('pstn', 'Outbound calls'), ('did', 'DID - Inbound calls'), ('pstn2did', 'Outbound calls to internal DID'), ('emergency', 'Emergency calls')], default='pstn', help_text='Type of calls.', max_length=10, verbose_name='Type of call')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dimproviderdestinations', to='pyfb_reporting.DimDate', verbose_name='date')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dimproviderdestinations', to='pyfb_direction.Destination')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dimproviderdestinations', to='pyfb_company.Provider', verbose_name='provider')),
            ],
            options={
                'db_table': 'pyfb_reporting_dim_prov_dest',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='DimProviderHangupcause',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hangupcause', models.CharField(blank=True, max_length=100, null=True, verbose_name='hangupcause')),
                ('total_calls', models.IntegerField(verbose_name='total calls')),
                ('direction', models.CharField(choices=[('pstn', 'Outbound calls'), ('did', 'DID - Inbound calls'), ('pstn2did', 'Outbound calls to internal DID'), ('emergency', 'Emergency calls')], default='pstn', help_text='Type of calls.', max_length=10, verbose_name='Type of call')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dimproviderhangupcauses', to='pyfb_reporting.DimDate', verbose_name='date')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dimproviderhangupcauses', to='pyfb_direction.Destination')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dimproviderhangupcauses', to='pyfb_company.Provider', verbose_name='provider')),
            ],
            options={
                'db_table': 'pyfb_reporting_dim_prov_hc',
                'ordering': ('-date',),
            },
        ),
        migrations.CreateModel(
            name='DimProviderSipHangupcause',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sip_hangupcause', models.CharField(blank=True, max_length=100, null=True, verbose_name='sip hangupcause')),
                ('total_calls', models.IntegerField(verbose_name='total calls')),
                ('direction', models.CharField(choices=[('pstn', 'Outbound calls'), ('did', 'DID - Inbound calls'), ('pstn2did', 'Outbound calls to internal DID'), ('emergency', 'Emergency calls')], default='pstn', help_text='Type of calls.', max_length=10, verbose_name='Type of call')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dimprovidersiphangupcauses', to='pyfb_reporting.DimDate', verbose_name='date')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dimprovidersiphangupcauses', to='pyfb_direction.Destination')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dimprovidersiphangupcauses', to='pyfb_company.Provider', verbose_name='provider')),
            ],
            options={
                'db_table': 'pyfb_reporting_dim_prov_sip_hc',
                'ordering': ('-date',),
            },
        ),
        migrations.AddField(
            model_name='dimcustomersiphangupcause',
            name='date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dimcustomersiphangupcauses', to='pyfb_reporting.DimDate', verbose_name='date'),
        ),
        migrations.AddField(
            model_name='dimcustomersiphangupcause',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dimcustomersiphangupcauses', to='pyfb_direction.Destination'),
        ),
        migrations.AddField(
            model_name='dimcustomerhangupcause',
            name='date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dimcustomerhangupcauses', to='pyfb_reporting.DimDate', verbose_name='date'),
        ),
        migrations.AddField(
            model_name='dimcustomerhangupcause',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dimcustomerhangupcauses', to='pyfb_direction.Destination'),
        ),
        migrations.AddField(
            model_name='dimcustomerdestination',
            name='date',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dimcustomerdestinations', to='pyfb_reporting.DimDate', verbose_name='date'),
        ),
        migrations.AddField(
            model_name='dimcustomerdestination',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dimcustomerdestinations', to='pyfb_direction.Destination'),
        ),
    ]
