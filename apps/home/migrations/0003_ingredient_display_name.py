# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170301_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='display_name',
            field=models.CharField(default='Default Ingredient Name', max_length=100),
            preserve_default=False,
        ),
    ]