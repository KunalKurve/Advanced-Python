from django.shortcuts import render

# Create your views here.
from django.contrib import admin
# from django import 

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")