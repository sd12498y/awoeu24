# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-24 19:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20171124_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('Processing', 'Processing'), ('Completed', 'Completed')], default='Processing', max_length=2),
        ),
        migrations.AddField(
            model_name='transaction',
            name='status',
            field=models.CharField(choices=[('Holding up by MyTutor', 'Holding up by MyTutor'), ('Transferred', 'Transferred'), ('Cancelled', 'Cancelled')], default='Holding up by MyTutor', max_length=2),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 24, 19, 10, 25, 707522, tzinfo=utc)),
        ),
    ]
