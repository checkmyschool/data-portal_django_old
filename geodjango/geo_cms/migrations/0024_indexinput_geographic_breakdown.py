# Generated by Django 2.2.5 on 2019-09-11 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo_cms', '0023_indexinput'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexinput',
            name='Geographic_Breakdown',
            field=models.CharField(default='School', max_length=20),
        ),
    ]
