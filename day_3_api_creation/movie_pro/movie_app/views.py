from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def movies(req):
    return HttpResponse("welcome to movies app!!")
