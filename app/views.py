from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

from django.http import HttpResponse
from . import raspberry


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def status(request):
    return JsonResponse(raspberry.status())
def switch(request, b):
    if b == 'open':
        raspberry.switch(True)
    elif b == 'high':
        raspberry.high(True)
    elif b == 'low':
        raspberry.high(False)
    elif b == 'close':
        raspberry.switch(False)
    return JsonResponse(raspberry.status())
