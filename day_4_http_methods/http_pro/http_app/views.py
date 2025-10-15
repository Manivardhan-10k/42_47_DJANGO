from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf  import csrf_exempt
import json

# Create your views here.
#cbv  fbv 
#decorator - it is a special function that adds additional functionality to the existing function 
     #        without changing its original functionality
#get -> to get data 

#post
#put
#patch
#delete

#CORS- Cross Origin Resource Sharing
#CSRF - Cross Site Request Forgery

# @csrf_exempt  # for ignoring the security for this view
# def welcome(something):
#     # for prop in dir(something):
#     #     print(prop)
#     # print(something.method)
#     return  HttpResponse("Welcome to django app!!")

details=[{
    "id_":1,
    "name":"saketh",
    "profession":"js developer",
    "salary":200000
},
         {
             "id_":2,
             "name":"anvesh",
             "profession":"react dev",
             "salary":500000
         }]

@csrf_exempt 
def welcome(request):
    if request.method =="GET":
        return HttpResponse ("welcome to get request!")
    else:
        return HttpResponse ("invalid method!")



#student/1

def details_view(req):
    return JsonResponse({"response":details})



#params
#query params

# urls/search?amazon
# url/user?mani&&password?secret


#url params
# products/1
# user/10
# brand/samsung


def single_user(req,id):
    for user in details:
        if id==user["id_"]:
            return JsonResponse({"user_data":user})
    return JsonResponse({"msg":"user does not exist!"})


#json.dumps  -- when sending 
#json .loads  -- when recieving
@csrf_exempt     
def register_user(req):
    # for prop in dir(req):
    #     print(prop,req[prop])
    user_data=json.loads(req.body)
    details.append(user_data)
    print(details)
    
    
    return HttpResponse("registration successful!")
    
    
    
