# Generated by Django 4.0 on 2024-04-20 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='z_avtobrand',
            fields=[
                ('BrandID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'z_avtobrand',
            },
        ),
        migrations.CreateModel(
            name='z_avtocolor',
            fields=[
                ('ColorID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'z_avtocolor',
            },
        ),
        migrations.CreateModel(
            name='z_avtomodel',
            fields=[
                ('ModelID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=100)),
                ('BrandID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avto_bs.z_avtobrand')),
            ],
            options={
                'db_table': 'z_avtomodel',
            },
        ),
    ]
