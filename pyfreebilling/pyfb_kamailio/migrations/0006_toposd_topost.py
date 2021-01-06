# Generated by Django 2.1.5 on 2019-02-26 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyfb_kamailio', '0005_auto_20190225_1803'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToposD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rectime', models.DateTimeField(db_index=True)),
                ('s_method', models.CharField(default='', max_length=64)),
                ('s_cseq', models.CharField(default='', max_length=64)),
                ('a_callid', models.CharField(db_index=True, default='', max_length=255)),
                ('a_uuid', models.CharField(db_index=True, default='', max_length=255)),
                ('b_uuid', models.CharField(db_index=True, default='', max_length=255)),
                ('a_contact', models.CharField(default='', max_length=128)),
                ('b_contact', models.CharField(default='', max_length=128)),
                ('as_contact', models.CharField(default='', max_length=128)),
                ('bs_contact', models.CharField(default='', max_length=128)),
                ('a_tag', models.CharField(default='', max_length=255)),
                ('b_tag', models.CharField(default='', max_length=255)),
                ('a_rr', models.TextField(blank=True, null=True)),
                ('b_rr', models.TextField(blank=True, null=True)),
                ('s_rr', models.TextField(blank=True, null=True)),
                ('iflags', models.IntegerField(default=0)),
                ('a_uri', models.CharField(default='', max_length=128)),
                ('b_uri', models.CharField(default='', max_length=128)),
                ('r_uri', models.CharField(default='', max_length=128)),
                ('a_srcaddr', models.CharField(default='', max_length=128)),
                ('b_srcaddr', models.CharField(default='', max_length=128)),
                ('a_socket', models.CharField(default='', max_length=128)),
                ('b_socket', models.CharField(default='', max_length=128)),
            ],
            options={
                'db_table': 'topos_d',
                'ordering': ('-pk',),
            },
        ),
        migrations.CreateModel(
            name='ToposT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rectime', models.DateTimeField(db_index=True)),
                ('s_method', models.CharField(default='', max_length=64)),
                ('s_cseq', models.CharField(default='', max_length=64)),
                ('a_callid', models.CharField(db_index=True, default='', max_length=255)),
                ('a_uuid', models.CharField(db_index=True, default='', max_length=255)),
                ('b_uuid', models.CharField(default='', max_length=255)),
                ('direction', models.IntegerField(default=0)),
                ('x_via', models.TextField(blank=True, null=True)),
                ('x_vbranch', models.CharField(db_index=True, default='', max_length=255)),
                ('x_rr', models.TextField(blank=True, null=True)),
                ('y_rr', models.TextField(blank=True, null=True)),
                ('s_rr', models.TextField(blank=True, null=True)),
                ('x_uri', models.CharField(default='', max_length=128)),
                ('a_contact', models.CharField(default='', max_length=128)),
                ('b_contact', models.CharField(default='', max_length=128)),
                ('as_contact', models.CharField(default='', max_length=128)),
                ('bs_contact', models.CharField(default='', max_length=128)),
                ('x_tag', models.CharField(default='', max_length=255)),
                ('a_tag', models.CharField(default='', max_length=255)),
                ('b_tag', models.CharField(default='', max_length=255)),
                ('a_srcaddr', models.CharField(default='', max_length=128)),
                ('b_srcaddr', models.CharField(default='', max_length=128)),
                ('a_socket', models.CharField(default='', max_length=128)),
                ('b_socket', models.CharField(default='', max_length=128)),
            ],
            options={
                'db_table': 'topos_t',
                'ordering': ('-pk',),
            },
        ),
    ]