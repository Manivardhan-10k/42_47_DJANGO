from django.urls import path
from . import views

urlpatterns=[
    # path("rev/", view=views.rev),
    path("all_users/",view=views.all_users),
    path("reg_user/",view=views.register),
    path("edit_user/<int:user_id>",view=views.edit_user)
    
]