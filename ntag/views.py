# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.views.decorators.http import requirse_POST
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import get_messages
from ntag.models import Tag


# Create your views here.

#from .models import Category, Product, Certificate, Increment

def TagAdd(request, category_slug=None):

	return render(request, 'index.html')

def TagDisplay(request, category_slug=None):
	tags = Tag.objects.all()
	return render(request, 'index.html', {'tags': tags})

def TagDisplayCurrent(request, tag_id):
	current = Tag.get_object_or_404(id=tag_id)
    return render(request, 'index.html', {'current': current})

