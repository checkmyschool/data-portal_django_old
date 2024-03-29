# Generated by Django 2.2.5 on 2019-09-10 02:04

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geo_cms', '0002_delete_cms2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='cms2017',
            fields=[
                ('field_1', models.BigIntegerField()),
                ('x', models.BigIntegerField()),
                ('school_yea', models.BigIntegerField()),
                ('school_id', models.BigIntegerField(blank=True, primary_key=True, serialize=False)),
                ('cluster', models.BigIntegerField()),
                ('remoteness', models.FloatField()),
                ('total_reci', models.BigIntegerField()),
                ('cct_percen', models.FloatField()),
                ('comments', models.CharField(max_length=254)),
                ('original_w', models.CharField(max_length=254)),
                ('nowater', models.BigIntegerField()),
                ('original_i', models.CharField(max_length=254)),
                ('no_interne', models.BigIntegerField()),
                ('noelec', models.BigIntegerField()),
                ('original_e', models.CharField(max_length=254)),
                ('instructio', models.BigIntegerField()),
                ('student_cl', models.FloatField()),
                ('total_teac', models.BigIntegerField()),
                ('student_te', models.FloatField()),
                ('remotene_1', models.FloatField()),
                ('cct_perc_1', models.FloatField()),
                ('nowater_sc', models.BigIntegerField()),
                ('no_inter_1', models.BigIntegerField()),
                ('noelec_sca', models.BigIntegerField()),
                ('scr_s', models.FloatField()),
                ('str_s', models.FloatField()),
                ('remotene_2', models.FloatField()),
                ('cct_perc_2', models.FloatField()),
                ('electricit', models.FloatField()),
                ('water_bool', models.FloatField()),
                ('internet_b', models.FloatField()),
                ('str_s2', models.FloatField()),
                ('scr_s2', models.FloatField()),
                ('accessibil', models.FloatField()),
                ('amenities', models.FloatField()),
                ('conditions', models.FloatField()),
                ('shi_score', models.FloatField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('school_nam', models.CharField(max_length=254)),
                ('region', models.CharField(max_length=254)),
                ('division', models.CharField(max_length=254)),
                ('province', models.CharField(max_length=254)),
                ('municipali', models.CharField(max_length=254)),
                ('district', models.CharField(max_length=254)),
                ('total_fema', models.BigIntegerField()),
                ('total_male', models.BigIntegerField()),
                ('total_enro', models.BigIntegerField()),
                ('ds_total', models.BigIntegerField()),
                ('cp_total', models.BigIntegerField()),
                ('dcm_total', models.BigIntegerField()),
                ('drcpau_tot', models.BigIntegerField()),
                ('dh_total', models.BigIntegerField()),
                ('autism_tot', models.BigIntegerField()),
                ('wcg_total', models.BigIntegerField()),
                ('eb_total', models.BigIntegerField()),
                ('hi_total', models.BigIntegerField()),
                ('id_total', models.BigIntegerField()),
                ('li_total', models.BigIntegerField()),
                ('md_total', models.BigIntegerField()),
                ('pd_total', models.BigIntegerField()),
                ('shp_total', models.BigIntegerField()),
                ('speech_tot', models.BigIntegerField()),
                ('vi_total', models.BigIntegerField()),
                ('ii_total', models.BigIntegerField()),
                ('p_total', models.BigIntegerField()),
                ('pwd_total', models.BigIntegerField()),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'db_table': 'cms2017',
                'managed': False,
            },
        ),
    ]
