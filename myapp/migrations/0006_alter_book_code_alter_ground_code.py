# Generated by Django 4.0.3 on 2022-03-11 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_ground_code_alter_book_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='code',
            field=models.CharField(default='5oNjp', max_length=5),
        ),
        migrations.AlterField(
            model_name='ground',
            name='code',
            field=models.CharField(default='5oNjp', max_length=5),
        ),
    ]
