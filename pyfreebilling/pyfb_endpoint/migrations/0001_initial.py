# Generated by Django 2.1.4 on 2018-12-18 16:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import partial_index
import pyfb_endpoint.models
import pyfb_endpoint.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pyfb_normalization', '0001_initial'),
        ('pyfb_company', '0004_auto_20181210_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Codec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('number', models.PositiveIntegerField()),
                ('ptime', models.PositiveIntegerField()),
                ('stereo', models.BooleanField(default=False)),
                ('rfc_name', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField(max_length=100)),
            ],
            options={
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='CustomerEndpoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(help_text='Ex.: customer SIP username, etc...', max_length=50, unique=True, verbose_name='username')),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled / disabled')),
                ('registration', models.BooleanField(default=True, help_text='Is registration needed for calling ? True, the phone needs to register with correct username/password. If false, you must specify a CIDR in SIP IP CIDR !', verbose_name='registration')),
                ('password', models.CharField(blank=True, default=pyfb_endpoint.models.random_string, help_text="It's recommended to use strong passwords for the endpoint.", max_length=64, verbose_name='password')),
                ('ha1', models.CharField(blank=True, default=pyfb_endpoint.models.random_string, help_text="It's recommended to use strong passwords for the endpoint. md5(username:realm:password)", max_length=128, verbose_name='ha1')),
                ('ha1b', models.CharField(blank=True, default=pyfb_endpoint.models.random_string, help_text="It's recommended to use strong passwords for the endpoint. md5(username@domain:realm:password)", max_length=128, verbose_name='ha1b')),
                ('rtp_ip', models.CharField(default='auto', help_text='Internal IP address/mask to bindto for RTP. Format : CIDR Ex. 192.168.1.0/32', max_length=100, verbose_name='RTP IP CIDR')),
                ('sip_ip', models.CharField(blank=True, help_text='Internal IP address/mask to bind to for SIP. Format : CIDR. Ex. 192.168.1.0/32', max_length=100, null=True, validators=[pyfb_endpoint.validators.validate_cidr], verbose_name='SIP IP CIDR')),
                ('sip_port', models.PositiveIntegerField(default=5060, verbose_name='SIP port')),
                ('sip_transport', models.CharField(choices=[('udp', 'udp'), ('tcp', 'tcp'), ('tls', 'tls')], default='udp', help_text='Which transport protocol to use for SIP messages', max_length=15, verbose_name='SIP transport protocol')),
                ('rtp_transport', models.CharField(choices=[('RTP/AVP', 'RTP/AVP')], default='RTP/AVP', help_text='Which transport protocol to use for RTP packets', max_length=15, verbose_name='RTP transport protocol')),
                ('rtp_tos', models.PositiveIntegerField(choices=[(0, '0 - CS0 - 0 Best effort'), (160, '160 - CS5 - 5 Critical'), (184, '184 - EF - 5 Critical')], default=184, help_text='Which TOS value to use for RTP packets', verbose_name='TOS value for RTP streams')),
                ('max_calls', models.TextField(default=1, help_text='max simultaneous calls allowed for this customer account.', verbose_name='max calls')),
                ('calls_per_second', models.TextField(default=10, help_text='maximum calls per second allowed for this customer endpoint.', verbose_name='max calls per second')),
                ('outbound_caller_id_name', models.CharField(blank=True, help_text='Caller ID name sent to provider on outbound calls.', max_length=50, verbose_name='callerID name')),
                ('outbound_caller_id_number', models.CharField(blank=True, help_text='Caller ID number sent to provider on outbound calls.', max_length=80, verbose_name='callerID num')),
                ('force_caller_id', models.BooleanField(default=False, verbose_name='force callerID')),
                ('masq_caller_id', models.BooleanField(default=False, verbose_name='masq callerID')),
                ('pai', models.BooleanField(default=False, help_text='put callerid in SIP PAI field if enabled', verbose_name='caller ID in PAI field')),
                ('pid', models.BooleanField(default=False, help_text='put callerid in SIP PID field if enabled', verbose_name='caller ID in PID field')),
                ('urgency_number', models.BooleanField(default=True, help_text='You have also to allow global routing option and define an urgency ratecard', verbose_name='allow urgency numbers')),
                ('insee_code', models.CharField(blank=True, help_text='Postal code, INSEE code ... for routing urgency number to the right urgency call center.', max_length=10, null=True, verbose_name='special code for routing urgency numbers')),
                ('fake_ring', models.BooleanField(default=False, help_text='Fake ring : Enabled / Disabled - Send a fake ring to the caller.', verbose_name='fake ring')),
                ('cli_debug', models.BooleanField(default=False, help_text='CLI debug : Enabled / Disabled - Permit to see all debug messages on cli.', verbose_name='CLI debug')),
                ('transcoding_allowed', models.BooleanField(default=False, help_text='If enabled, calls could be transcoded. be careful, as it is an expensive cpu task.', verbose_name='allow transcoding calls')),
                ('recording_allowed', models.BooleanField(default=False, help_text='If enabled, calls could be recorded. be careful on available space.', verbose_name='allow recording calls')),
                ('recording_always', models.BooleanField(default=False, help_text='If enabled, all calls will be recorded. be careful on available space.', verbose_name='record all calls')),
                ('recording_limit', models.PositiveIntegerField(default=30, help_text='how many Mo will be available for recording storage.', verbose_name='recording space storage')),
                ('recording_retention', models.PositiveIntegerField(default=30, help_text='how many days a recording will be available. After, it will be deleted by automatic job', verbose_name='retention days for recording')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('callee_norm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='caleenormrules_c', to='pyfb_normalization.NormalizationGrp', verbose_name='Destination number normalization rules for outbound call')),
                ('callee_norm_in', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='caleenormrulesin_c', to='pyfb_normalization.NormalizationGrp', verbose_name='Destination number normalization rules for inbound call')),
                ('callerid_norm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='calleridnormrules_c', to='pyfb_normalization.NormalizationGrp', verbose_name='CallerID normalization rules for outbound call')),
                ('callerid_norm_in', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='calleridnormrulesin_c', to='pyfb_normalization.NormalizationGrp', verbose_name='CallerID normalization rules for inbound call')),
                ('codec_list', models.ManyToManyField(related_name='codecs_c', to='pyfb_endpoint.Codec')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='pyfb_company.Customer', verbose_name='customer')),
            ],
            options={
                'ordering': ('customer', 'name'),
                'db_table': 'pyfb_endpoint_customer',
                'verbose_name_plural': 'customer endpoints',
                'verbose_name': 'customer endpoint',
            },
        ),
        migrations.CreateModel(
            name='ProviderEndpoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='name')),
                ('enabled', models.BooleanField(default=True, verbose_name='enabled / disabled')),
                ('username', models.CharField(blank=True, default='', max_length=35, verbose_name='username')),
                ('password', models.CharField(blank=True, default='', max_length=64, verbose_name='password')),
                ('register', models.BooleanField(default=False, verbose_name='register')),
                ('realm', models.CharField(blank=True, default='', help_text='Authentication realm. Same as gateway name, if blank.', max_length=64, verbose_name='realm')),
                ('from_domain', models.CharField(blank=True, default='', help_text='Domain to use in from field. Same as realm if blank.', max_length=50, verbose_name='from domain')),
                ('expire_seconds', models.PositiveIntegerField(default=3600, null=True, verbose_name='expire seconds')),
                ('retry_seconds', models.PositiveIntegerField(default=30, help_text='How many seconds before a retry when a failure or timeout occurs', null=True, verbose_name='retry seconds')),
                ('max_calls', models.PositiveIntegerField(default=30, help_text='max simultaneous calls allowed for this customer account.', verbose_name='max calls')),
                ('calls_per_second', models.PositiveIntegerField(default=10, help_text='maximum calls per second allowed for this gateway.', verbose_name='max calls per second')),
                ('sip_proxy', models.CharField(default='', help_text='IP if register is False.', max_length=128, verbose_name='proxy')),
                ('sip_transport', models.CharField(choices=[('udp', 'udp'), ('tcp', 'tcp'), ('tls', 'tls')], default='udp', help_text='Which transport to use for SIP messages', max_length=15, verbose_name='SIP transport protocol')),
                ('sip_port', models.PositiveIntegerField(default='5060', help_text='Gateway SIP port - Default 5060 -.', verbose_name='SIP port')),
                ('rtp_transport', models.CharField(choices=[('RTP/AVP', 'RTP/AVP')], default='RTP/AVP', help_text='Which transport protocol to use for RTP packets', max_length=15, verbose_name='RTP transport protocol')),
                ('rtp_tos', models.PositiveIntegerField(choices=[(0, '0 - CS0 - 0 Best effort'), (160, '160 - CS5 - 5 Critical'), (184, '184 - EF - 5 Critical')], default=184, help_text='Which TOS value to use for RTP packets', verbose_name='TOS value for RTP streams')),
                ('prefix', models.CharField(blank=True, default='', max_length=15, verbose_name='prefix')),
                ('suffix', models.CharField(blank=True, default='', max_length=15, verbose_name='suffix')),
                ('caller_id_in_from', models.BooleanField(default=True, help_text='Use the callerid of an inbound call in the from field on outbound calls via this gateway.', verbose_name='caller ID in From field')),
                ('pid', models.BooleanField(default=False, help_text='put callerid in SIP PID field if enabled', verbose_name='caller ID in PID field')),
                ('pai', models.BooleanField(default=False, help_text='put callerid in SIP PAI field if enabled', verbose_name='caller ID in PAI field')),
                ('callee_norm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='caleenormrules_p', to='pyfb_normalization.NormalizationGrp', verbose_name='Destination number normalization rules for outbound call')),
                ('callee_norm_in', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='caleenormrulesin_p', to='pyfb_normalization.NormalizationGrp', verbose_name='Destination number normalization rules for inbound call')),
                ('callerid_norm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='calleridnormrules_p', to='pyfb_normalization.NormalizationGrp', verbose_name='CallerID normalization rules for outbound call')),
                ('callerid_norm_in', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='calleridnormrulesin_p', to='pyfb_normalization.NormalizationGrp', verbose_name='CallerID normalization rules for inbound call')),
                ('codec_list', models.ManyToManyField(related_name='codecs_p', to='pyfb_endpoint.Codec')),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='providers_p', to='pyfb_company.Provider', verbose_name='Provider')),
            ],
            options={
                'ordering': ('provider', 'name'),
                'db_table': 'pyfb_endpoint_provider',
                'verbose_name_plural': 'provider endpoints',
                'verbose_name': 'provider endpoint',
            },
        ),
        migrations.AddIndex(
            model_name='providerendpoint',
            index=partial_index.PartialIndex(fields=['name', 'callerid_norm'], name='pyfb_endpoi_name_6e3cf8_partial', unique=True, where_postgresql='enabled = True', where_sqlite=''),
        ),
        migrations.AddIndex(
            model_name='providerendpoint',
            index=partial_index.PartialIndex(fields=['name', 'callee_norm'], name='pyfb_endpoi_name_e54096_partial', unique=True, where_postgresql='enabled = True', where_sqlite=''),
        ),
        migrations.AddIndex(
            model_name='providerendpoint',
            index=partial_index.PartialIndex(fields=['name', 'callerid_norm_in'], name='pyfb_endpoi_name_3ead03_partial', unique=True, where_postgresql='enabled = True', where_sqlite=''),
        ),
        migrations.AddIndex(
            model_name='providerendpoint',
            index=partial_index.PartialIndex(fields=['name', 'callee_norm_in'], name='pyfb_endpoi_name_48168f_partial', unique=True, where_postgresql='enabled = True', where_sqlite=''),
        ),
        migrations.AddIndex(
            model_name='customerendpoint',
            index=partial_index.PartialIndex(fields=['name', 'callerid_norm'], name='pyfb_endpoi_name_3a00d3_partial', unique=True, where_postgresql='enabled = True', where_sqlite=''),
        ),
        migrations.AddIndex(
            model_name='customerendpoint',
            index=partial_index.PartialIndex(fields=['name', 'callee_norm'], name='pyfb_endpoi_name_f5c867_partial', unique=True, where_postgresql='enabled = True', where_sqlite=''),
        ),
        migrations.AddIndex(
            model_name='customerendpoint',
            index=partial_index.PartialIndex(fields=['name', 'callerid_norm_in'], name='pyfb_endpoi_name_0079d2_partial', unique=True, where_postgresql='enabled = True', where_sqlite=''),
        ),
        migrations.AddIndex(
            model_name='customerendpoint',
            index=partial_index.PartialIndex(fields=['name', 'callee_norm_in'], name='pyfb_endpoi_name_d7f6c3_partial', unique=True, where_postgresql='enabled = True', where_sqlite=''),
        ),
    ]
