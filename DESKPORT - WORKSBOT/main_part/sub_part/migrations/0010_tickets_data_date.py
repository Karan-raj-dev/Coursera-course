# Generated by Django 3.1.7 on 2021-03-23 07:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_part', '0009_tickets_data_problemid'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets_data',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
