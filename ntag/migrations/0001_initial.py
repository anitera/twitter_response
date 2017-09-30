# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=140, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='twitter_response/static/img/portfolio')),
            ],
        ),
    ]
