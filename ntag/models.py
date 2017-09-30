# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tag(models.Model):
	tag = models.CharField(max_length=140, unique=True)
	bad_words = models.ImageField(upload_to='tag', blank=True, null=True)
	common_words = models.ImageField(upload_to='tag', blank=True, null=True)
	good_words = models.ImageField(upload_to='tag', blank=True, null=True)
	piechart = models.ImageField(upload_to='tag', blank=True, null=True)




