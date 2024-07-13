# Generated by Django 5.0.6 on 2024-07-09 01:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_rename_reviewmode_reviewmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewmodel',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
