# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-16 11:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('linker', '0003_auto_20151216_1251'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Settings',
        ),
    ]
