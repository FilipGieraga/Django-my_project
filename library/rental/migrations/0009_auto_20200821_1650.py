# Generated by Django 3.0.7 on 2020-08-21 14:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0008_borrowed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowed',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2020, 11, 19, 16, 49, 59, 789785)),
        ),
    ]
