# Generated by Django 2.2.5 on 2019-09-13 13:42

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo_cms', '0027_auto_20190913_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regions_simple',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(geography=True, srid=4326),
        ),
    ]
