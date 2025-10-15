from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

# @csrf_exempt
# def rev(request):
    # user_Data=json.loads(request.body)
    # print(user_Data)
    
    # print(request.POST.get("username"))
    # print(request.POST.get("branch"))
    # print(request.FILES.get("profile_pic"))
    
    # return HttpResponse("welcome to django!!")



# form data 

#
# json data




details=[{"id":1,"name":"ashwini","branch":47},{"id":2,"name":"vigneshwari","branch":47},{"id":3,"name":"bhargav","branch":47},{"id":4,"name":"yashwanth","branch":47}]


def all_users(req):
    return JsonResponse({"user_data":details})

@csrf_exempt
def register(req):
    user_details=json.loads(req.body)
    details.append(user_details)
    print(details)
    return HttpResponse("registration successful!")
    
@csrf_exempt
def edit_user(req,user_id):
    user_data=json.loads(req.body)#{name:yash}
    for user in details:
        if user["id"]==user_id:
            for key1 in user:# id name   branch
                for key2 in user_data:  #name
                    if key1==key2:
                        user[key1]=user_data[key2] #user[name]=yash
    return JsonResponse({"user_id":user_id})
    


# MVT
#model  - db table
#view
#template

    
    