# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-03 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190802_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='status',
            field=models.CharField(choices=[('a', 'Approved'), ('s', 'Submitted'), ('r', 'Rejected')], default='s', max_length=1),
            preserve_default=False,
        ),
    ]
