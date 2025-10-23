from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Employee
from django.http import HttpResponse,JsonResponse
from .serializer import EmpSerializer
# Create your views here.

#form 
#json

#ORM -> Object Relational Mapping
@csrf_exempt #a function that adds additional functionality without changing the original function
def reg_user(req):
    user_data=json.loads(req.body)
    print(user_data)
    new_user=Employee.objects.create(emp_id=user_data["emp_id"],emp_name=user_data["emp_name"],emp_mob=user_data["emp_mob"],emp_email=user_data["emp_email"])
    return HttpResponse("user created!")
    
    
    
def all_users(req):
    # all_user_data=Employee.objects.all().values()
    # data_list=[]
    # for emp in all_user_data:
    #     data_list.append(emp)
    # return JsonResponse({"user_data":data_list})
    data=Employee.objects.all()
    all_users=EmpSerializer(data,many=True)
    return JsonResponse({"data":all_users.data})


def update_user(req,id):
    try:
        single_user=Employee.objects.get(emp_id=id)
        user_data=json.loads(req.body)
        serializer=EmpSerializer(single_user,data=user_data,partial=True)# record to be updated/ update data   / partial update
        if serializer.is_valid():
         serializer.save()
         return HttpResponse("user updated!")
        else:
         return HttpResponse("invalid data")

    except:
       return HttpResponse("user not found!")
   
   
def delete_user(req,id):
    try:
     single_user=Employee.objects.get(emp_id=id)
     single_user.delete()
     return HttpResponse("user deleted!")
    except:
        return HttpResponse("user not found!")


    
    
#AWS Azure 

# instance   -  ec2   --  render
# database  -   rds   --  aiven
# storage   -   s3     -- cloudinary
    