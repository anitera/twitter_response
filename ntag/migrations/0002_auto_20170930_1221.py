# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ntag', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]