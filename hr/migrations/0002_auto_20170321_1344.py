# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee_achievement',
            old_name='units_points',
            new_name='points_on_unit_task',
        ),
        migrations.AddField(
            model_name='employee_achievement',
            name='total_units_points',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=12),
        ),
    ]
