from django.urls import path 
from . import views

urlpatterns=[
    path("details/",view=views.details),
    path("reg_user/",view=views.reg_user)
]