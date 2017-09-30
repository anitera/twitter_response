from django.shortcuts import render
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import get_messages
from ntag.models import Tag
from ntag.forms import InsertTag
#from .gather_data import searchtag
#from .sentemet_analysys import semantic_script


# Create your views here.

#from .models import Category, Product, Certificate, Increment

def Taglist(request, category_slug=None):
	form = InsertTag(request.POST)
        # check whether it's valid:
        if form.is_valid():
        	tag = form.cleaned_data['tag']
        	#searchtag.datarun(tag)
        	#sentement()

	tags = Tag.objects.all()
	return render(request, 'index.html', {'tags': tags})