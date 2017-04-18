# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 08:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('promgen', '0021_auto_20161228_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='audit',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='audit',
            name='object_id',
            field=models.PositiveIntegerField(default=0),
        ),
    ]