from django.shortcuts import render
from .models import Student
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import  csrf_exempt #cross site request forgery
import json

# Create your views here.

#MVT 


def get_users(req):
    if req.method=="GET":
        stu_data=Student.objects.all() #for fetching all the records from the table   # queryset with object
        dict_data=stu_data.values() #for converting the query object into dictionary
        list_data=list(dict_data) # for converting queryobject into python list
        return JsonResponse({"all_data":list_data})
        
        
        
@csrf_exempt
def reg_user(req):
    if req.method=="POST":  #form / json
        user_data=json.loads(req.body)
        id=user_data["stu_id"]
        name=user_data["stu_name"]
        branch=user_data["stu_branch"]
        mob=user_data["stu_mob"]
        new_stu=Student.objects.create(stu_id=id,stu_name=name,stu_branch=branch,stu_mob=mob)
        return JsonResponse({"msg":"user registered successfully"})
        
        
        