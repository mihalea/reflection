# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-09 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linker', '0008_auto_20151216_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.FileField(default=None, upload_to='images'),
            preserve_default=False,
        ),
    ]