# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='paint_points',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True),
        ),
    ]