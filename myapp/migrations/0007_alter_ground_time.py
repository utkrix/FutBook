# Generated by Django 4.0.3 on 2022-03-11 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_nos_ground_gname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ground',
            name='time',
            field=models.CharField(max_length=30),
        ),
    ]