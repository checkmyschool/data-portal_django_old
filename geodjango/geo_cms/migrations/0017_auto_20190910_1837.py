# Generated by Django 2.2.5 on 2019-09-10 18:37

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geo_cms', '0016_auto_20190910_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regions2',
            name='geom',
            field=django.contrib.gis.db.models.fields.PolygonField(geography=True, srid=4326),
        ),
    ]