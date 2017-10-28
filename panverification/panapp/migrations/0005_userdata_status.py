# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panapp', '0004_auto_20171028_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='status',
            field=models.CharField(choices=[(1, b'Pending'), (2, b'Completed')], default=1, max_length=2),
        ),
    ]
