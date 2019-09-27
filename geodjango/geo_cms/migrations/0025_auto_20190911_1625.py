# Generated by Django 2.2.5 on 2019-09-11 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_cms', '0024_indexinput_geographic_breakdown'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexinput',
            name='Accessibility_Category_Weight',
            field=models.FloatField(default=0.35),
        ),
        migrations.AddField(
            model_name='indexinput',
            name='Amentities_Category_Weight',
            field=models.FloatField(default=0.35),
        ),
        migrations.AddField(
            model_name='indexinput',
            name='Conditions_Category_Weight',
            field=models.FloatField(default=0.3),
        ),
    ]
