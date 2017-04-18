# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promgen', '0015_delete_stat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterUniqueTogether(
            name='farm',
            unique_together=set([('name', 'source')]),
        ),
    ]