# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launding', '0003_auto_20170301_0443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='time',
        ),
        migrations.AlterField(
            model_name='people',
            name='ipadress',
            field=models.CharField(default='88.201.141.79', max_length=128),
        ),
    ]