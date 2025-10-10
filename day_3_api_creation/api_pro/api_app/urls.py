from django.urls import path 
from . import views

urlpatterns=[
    path("wish/",view=views.greetings),
    path("message/",view=views.message)
    
]