from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from . import raspberry


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def status(request):
    return HttpResponse(raspberry.status())
def switch(request, b):
    if b == 'open':
        raspberry.switch(True)
    else:
        raspberry.switch(False)
    return HttpResponse(raspberry.status())
