# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 00:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('launding', '0004_auto_20170302_0319'),
    ]

    operations = [
        migrations.DeleteModel(
            name='People',
        ),
    ]