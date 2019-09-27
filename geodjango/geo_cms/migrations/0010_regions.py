# Generated by Django 2.2.5 on 2019-09-10 06:43

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_cms', '0009_delete_regions'),
    ]

    operations = [
        migrations.CreateModel(
            name='regions',
            fields=[
                ('region_name', models.CharField(blank=True, max_length=80, primary_key=True, serialize=False)),
                ('shape_length', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('x', models.IntegerField()),
                ('unnm_0', models.FloatField()),
                ('school_year', models.FloatField()),
                ('school_id', models.FloatField()),
                ('remoteness_index', models.FloatField()),
                ('total_recieving_cct', models.FloatField()),
                ('cct_percentage', models.FloatField()),
                ('original_water_boolean', models.FloatField()),
                ('nowater', models.FloatField()),
                ('original_internet_boolean', models.FloatField()),
                ('no_internet', models.FloatField()),
                ('noelec', models.FloatField()),
                ('original_electricity_boolean', models.FloatField()),
                ('instructional_rooms', models.FloatField()),
                ('student_classroom_ratio', models.FloatField()),
                ('total_teachers', models.FloatField()),
                ('student_teacher_ratio', models.FloatField()),
                ('remoteness_index_scaled', models.FloatField()),
                ('cct_percentage_scaled', models.FloatField()),
                ('nowater_scaled', models.FloatField()),
                ('no_internet_scaled', models.FloatField()),
                ('noelec_scaled', models.FloatField()),
                ('student_classroom_ratio_scaled', models.FloatField()),
                ('student_teacher_ratio_scaled', models.FloatField()),
                ('remoteness_index_scaled2', models.FloatField()),
                ('cct_percentage_scaled2', models.FloatField()),
                ('electricity_boolean_reversed_scaled2', models.FloatField()),
                ('water_boolean_reversed_scaled2', models.FloatField()),
                ('internet_boolean_reversed_scaled2', models.FloatField()),
                ('student_teacher_ratio_scaled2', models.FloatField()),
                ('student_classroom_ratio_scaled2', models.FloatField()),
                ('accessibility', models.FloatField()),
                ('amenities', models.FloatField()),
                ('conditions', models.FloatField()),
                ('shi_score', models.FloatField()),
                ('longitude', models.FloatField()),
                ('total_female', models.FloatField()),
                ('total_male', models.FloatField()),
                ('total_enrollment', models.FloatField()),
                ('ds_total', models.FloatField()),
                ('cp_total', models.FloatField()),
                ('dcm_total', models.FloatField()),
                ('drcpau_total', models.FloatField()),
                ('dh_total', models.FloatField()),
                ('autism_total', models.FloatField()),
                ('wcg_total', models.FloatField()),
                ('eb_total', models.FloatField()),
                ('hi_total', models.FloatField()),
                ('id_total', models.FloatField()),
                ('li_total', models.FloatField()),
                ('md_total', models.FloatField()),
                ('pd_total', models.FloatField()),
                ('shp_total', models.FloatField()),
                ('speech_total', models.FloatField()),
                ('vi_total', models.FloatField()),
                ('ii_total', models.FloatField()),
                ('p_total', models.FloatField()),
                ('pwd_total', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
            options={
                'db_table': 'regions',
                'managed': False,
            },
        ),
    ]
