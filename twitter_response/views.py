from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import get_messages


# Create your views here.

#from .models import Category, Product, Certificate, Increment

def Teglist(request, category_slug=None):

    return render(request, 'index.html')




