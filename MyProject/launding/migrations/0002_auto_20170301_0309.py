# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 00:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launding', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='ip',
            field=models.CharField(default='ABC', max_length=128),
        ),
        migrations.AddField(
            model_name='people',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]