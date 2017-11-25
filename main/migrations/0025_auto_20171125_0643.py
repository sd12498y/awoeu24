# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-24 22:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20171125_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='action',
            field=models.CharField(choices=[('Add Value', 'Add Value'), ('Tutorial Payment', 'Tutorial Payment'), ('Withdrawl', 'Withdrawl')], max_length=30),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 24, 22, 43, 23, 400073, tzinfo=utc)),
        ),
    ]
