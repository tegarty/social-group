# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-05 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image_url',
            field=models.URLField(default='http://via.placeholder.com/200x200'),
        ),
    ]
