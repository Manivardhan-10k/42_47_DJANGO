from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import UserReg

# Create your views here.

#form data        json data
#name 
#email
#password
#mobile


#multi media 


def validate_file(file_obj):
    # Check file size (limit 5MB)
    max_size = 5 * 1024 * 1024
    if file_obj.size > max_size:
        return False, 'File too large. Max size is 5MB.'

    # Check content type (MIME)
    allowed_types = ['image/jpeg', 'image/png']
    if file_obj.content_type not in allowed_types:
        return False, 'Invalid file type. Allowed: JPG, PNG'

    return True, 'Valid file'
@csrf_exempt
def reg_user(req):
    user_name=req.POST.get("name")
    user_email=req.POST.get("email")
    user_mob=req.POST.get("mob")
    file_obj=req.FILES["profile_pic"]
    
    is_valid_file,msg=validate_file(file_obj)
    
    if is_valid_file:
        pass 
    else:
        return HttpResponse (msg)    
    
    #RAM
    #ROM - Read Only Memory 
    ##s3
    new_user=UserReg.objects.create(name=user_name,email=user_email,mobile=user_mob,pic=file_obj)
    return HttpResponse("reg!")


# bytes
#0/1 - bit
# 8 bits - byte
#kb 1024        mb1024kb   gb1024    tb1024    pb1024  zb1024



#5*60 
#1*60*60

#5*1024*1024 


# name -  20-25 (alphabets)
# email- 30 
# mobile - 9 8 7 6  -- 10digits 
# profile - size and type 