# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season_stats',
            name='player_id',
            field=models.CharField(max_length=200),
        ),
    ]
