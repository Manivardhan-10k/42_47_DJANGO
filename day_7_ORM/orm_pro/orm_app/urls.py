from django.urls import path 
from . import views

urlpatterns=[
    
    path("get_users/",view=views.get_users),
    path("reg_user/",view=views.reg_user),
    # path("update_user/",view=views.update_user),
    # path("delete_user/",view=views.delete_user)
]