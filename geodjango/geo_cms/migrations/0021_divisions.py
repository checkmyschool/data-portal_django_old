# Generated by Django 2.2.5 on 2019-09-11 00:07

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_cms', '0020_auto_20190910_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='divisions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('divsn_n', models.CharField(max_length=80)),
                ('shp_lng', models.FloatField(blank=True, null=True)),
                ('shap_ar', models.FloatField(blank=True, null=True)),
                ('x', models.IntegerField(blank=True, null=True)),
                ('unnm_0', models.FloatField(blank=True, null=True)),
                ('schl_yr', models.FloatField(blank=True, null=True)),
                ('schol_d', models.FloatField(blank=True, null=True)),
                ('rmtnss_field', models.FloatField(blank=True, null=True)),
                ('ttl_rc_field', models.FloatField(blank=True, null=True)),
                ('cct_prc', models.FloatField(blank=True, null=True)),
                ('orgnl_w_field', models.FloatField(blank=True, null=True)),
                ('nowater', models.FloatField(blank=True, null=True)),
                ('orgnl_n_field', models.FloatField(blank=True, null=True)),
                ('n_ntrnt', models.FloatField(blank=True, null=True)),
                ('noelec', models.FloatField(blank=True, null=True)),
                ('orgnl_l_field', models.FloatField(blank=True, null=True)),
                ('inst_field', models.FloatField(blank=True, null=True)),
                ('ttl_tch', models.FloatField(blank=True, null=True)),
                ('rmtns_field', models.FloatField(blank=True, null=True)),
                ('cct_pr_field', models.FloatField(blank=True, null=True)),
                ('nwtr_sc', models.FloatField(blank=True, null=True)),
                ('n_ntrn_field', models.FloatField(blank=True, null=True)),
                ('nlc_scl', models.FloatField(blank=True, null=True)),
                ('stdnt_c_field', models.FloatField(blank=True, null=True)),
                ('stdnt_t_field', models.FloatField(blank=True, null=True)),
                ('rmtn_2', models.FloatField(blank=True, null=True)),
                ('cct_p_2', models.FloatField(blank=True, null=True)),
                ('elc_2', models.FloatField(blank=True, null=True)),
                ('wtr_2', models.FloatField(blank=True, null=True)),
                ('int_2', models.FloatField(blank=True, null=True)),
                ('stdnt_t_2', models.FloatField(blank=True, null=True)),
                ('stdnt_c_2', models.FloatField(blank=True, null=True)),
                ('accssbl', models.FloatField(blank=True, null=True)),
                ('amenits', models.FloatField(blank=True, null=True)),
                ('condtns', models.FloatField(blank=True, null=True)),
                ('shi_scr', models.FloatField(blank=True, null=True)),
                ('longitd', models.FloatField(blank=True, null=True)),
                ('ttl_fml', models.FloatField(blank=True, null=True)),
                ('totl_ml', models.FloatField(blank=True, null=True)),
                ('ttl_nrl', models.FloatField(blank=True, null=True)),
                ('ds_totl', models.FloatField(blank=True, null=True)),
                ('cp_totl', models.FloatField(blank=True, null=True)),
                ('dcm_ttl', models.FloatField(blank=True, null=True)),
                ('drcp_tt', models.FloatField(blank=True, null=True)),
                ('dh_totl', models.FloatField(blank=True, null=True)),
                ('atsm_tt', models.FloatField(blank=True, null=True)),
                ('wcg_ttl', models.FloatField(blank=True, null=True)),
                ('eb_totl', models.FloatField(blank=True, null=True)),
                ('hi_totl', models.FloatField(blank=True, null=True)),
                ('id_totl', models.FloatField(blank=True, null=True)),
                ('li_totl', models.FloatField(blank=True, null=True)),
                ('md_totl', models.FloatField(blank=True, null=True)),
                ('pd_totl', models.FloatField(blank=True, null=True)),
                ('shp_ttl', models.FloatField(blank=True, null=True)),
                ('spch_tt', models.FloatField(blank=True, null=True)),
                ('vi_totl', models.FloatField(blank=True, null=True)),
                ('ii_totl', models.FloatField(blank=True, null=True)),
                ('p_total', models.FloatField(blank=True, null=True)),
                ('pwd_ttl', models.FloatField(blank=True, null=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(geography=True, srid=4326)),
            ],
        ),
    ]
