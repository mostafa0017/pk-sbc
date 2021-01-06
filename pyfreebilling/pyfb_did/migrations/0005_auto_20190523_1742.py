# Generated by Django 2.1.5 on 2019-05-23 17:42

from django.db import migrations
import migrate_sql.operations


class Migration(migrations.Migration):

    dependencies = [
        ('pyfb_kamailio', '0009_auto_20190523_1647'),
        ('pyfb_endpoint', '0010_customerendpoint_domain'),
        ('pyfb_did', '0004_auto_20190130_1838'),
    ]

    operations = [
        migrate_sql.operations.ReverseAlterSQL(
            name='dbaliases_view',
            sql='DROP VIEW IF EXISTS dbaliases CASCADE;',
            reverse_sql="DROP VIEW IF EXISTS dbaliases CASCADE; CREATE OR REPLACE VIEW dbaliases AS  SELECT row_number() OVER () AS id,  d.number AS alias_username,  '' AS alias_domain,  cd.name AS username,  '' AS domain FROM pyfb_did_routes dr LEFT JOIN pyfb_did d  ON dr.contract_did_id = d.id AND dr.type = 's' LEFT JOIN pyfb_endpoint_customer cd  ON dr.trunk_id = cd.id ",
        ),
        migrate_sql.operations.AlterSQL(
            name='dbaliases_view',
            sql="DROP VIEW IF EXISTS dbaliases CASCADE; CREATE OR REPLACE VIEW dbaliases AS  SELECT row_number() OVER () AS id,  d.number AS alias_username,  '' AS alias_domain,  cd.name AS username,  ud.domain AS domain FROM pyfb_did_routes dr LEFT JOIN pyfb_did d  ON dr.contract_did_id = d.id AND dr.type = 's' LEFT JOIN pyfb_endpoint_customer cd  ON dr.trunk_id = cd.id LEFT JOIN domain ud  ON ud.id = cd.domain_id;",
            reverse_sql='DROP VIEW IF EXISTS dbaliases CASCADE;',
        ),
    ]
