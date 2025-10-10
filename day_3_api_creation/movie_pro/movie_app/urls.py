from django.urls import path 
from . import views


urlpatterns=[
    path("select/",view=views.movies)
]