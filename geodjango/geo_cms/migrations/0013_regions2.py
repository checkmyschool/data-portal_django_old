# Generated by Django 2.2.5 on 2019-09-10 18:25

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_cms', '0012_regions'),
    ]

    operations = [
        migrations.CreateModel(
            name='regions2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regn_nm', models.CharField(max_length=80)),
                ('shp_lng', models.FloatField()),
                ('shap_ar', models.FloatField()),
                ('x', models.IntegerField()),
                ('unnm_0', models.FloatField()),
                ('schl_yr', models.FloatField()),
                ('schol_d', models.FloatField()),
                ('rmtnss_field', models.FloatField()),
                ('ttl_rc_field', models.FloatField()),
                ('cct_prc', models.FloatField()),
                ('orgnl_w_field', models.FloatField()),
                ('nowater', models.FloatField()),
                ('orgnl_n_field', models.FloatField()),
                ('n_ntrnt', models.FloatField()),
                ('noelec', models.FloatField()),
                ('orgnl_l_field', models.FloatField()),
                ('inst_field', models.FloatField()),
                ('ttl_tch', models.FloatField()),
                ('rmtns_field', models.FloatField()),
                ('cct_pr_field', models.FloatField()),
                ('nwtr_sc', models.FloatField()),
                ('n_ntrn_field', models.FloatField()),
                ('nlc_scl', models.FloatField()),
                ('stdnt_c_field', models.FloatField()),
                ('stdnt_t_field', models.FloatField()),
                ('rmtn_2', models.FloatField()),
                ('cct_p_2', models.FloatField()),
                ('elc_2', models.FloatField()),
                ('wtr_2', models.FloatField()),
                ('int_2', models.FloatField()),
                ('stdnt_t_2', models.FloatField()),
                ('stdnt_c_2', models.FloatField()),
                ('accssbl', models.FloatField()),
                ('amenits', models.FloatField()),
                ('condtns', models.FloatField()),
                ('shi_scr', models.FloatField()),
                ('longitd', models.FloatField()),
                ('ttl_fml', models.FloatField()),
                ('totl_ml', models.FloatField()),
                ('ttl_nrl', models.FloatField()),
                ('ds_totl', models.FloatField()),
                ('cp_totl', models.FloatField()),
                ('dcm_ttl', models.FloatField()),
                ('drcp_tt', models.FloatField()),
                ('dh_totl', models.FloatField()),
                ('atsm_tt', models.FloatField()),
                ('wcg_ttl', models.FloatField()),
                ('eb_totl', models.FloatField()),
                ('hi_totl', models.FloatField()),
                ('id_totl', models.FloatField()),
                ('li_totl', models.FloatField()),
                ('md_totl', models.FloatField()),
                ('pd_totl', models.FloatField()),
                ('shp_ttl', models.FloatField()),
                ('spch_tt', models.FloatField()),
                ('vi_totl', models.FloatField()),
                ('ii_totl', models.FloatField()),
                ('p_total', models.FloatField()),
                ('pwd_ttl', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
    ]
