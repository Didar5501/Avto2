# Generated by Django 5.0.4 on 2024-04-23 20:52

import geoposition.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='position',
            field=geoposition.fields.GeopositionField(max_length=42, null=True),
        ),
    ]
