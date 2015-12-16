# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-16 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linker', '0002_remove_project_alias'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_username', models.CharField(max_length=64)),
            ],
        ),
        migrations.RenameField(
            model_name='project',
            old_name='latest_sha',
            new_name='sha',
        ),
        migrations.RemoveField(
            model_name='project',
            name='origin',
        ),
        migrations.AddField(
            model_name='project',
            name='watched',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]