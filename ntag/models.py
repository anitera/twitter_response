# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tag(models.Model):
	tag = models.CharField(max_length=140, unique=True)
	image = models.ImageField(upload_to='', blank=True, null=True)


