# Generated by Django 2.2.5 on 2019-09-10 18:54

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_cms', '0018_auto_20190910_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='regions3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_nam', models.CharField(max_length=254)),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
    ]
