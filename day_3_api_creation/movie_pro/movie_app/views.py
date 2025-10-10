from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def movies(req):
    for prop in dir(req):
        print(prop)
    return HttpResponse("welcome to movies app!!")
