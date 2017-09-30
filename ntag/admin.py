# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models

# Register your models here.
class TagAdmin(admin.ModelAdmin):
	list_display = ('tag',)

admin.site.register(models.Tag, TagAdmin)