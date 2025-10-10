from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


#FBV  -> Function Based View
#CBV  -> Class Based View 


def greetings(self):
    return HttpResponse("hello from django!!")

def message(req):
    print(dir(req))
    return HttpResponse("message api is working")