from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def user_login(request):
    if request.method=="POST":
        redg_no=request.POST.get("redg_no")
        password=request.POST.get("password")
        user=authenticate(request,usernmae=redg_no,password=password)
        if user is None:
            print(redg_no,password)
            return render(request,"user_profile/login.html")
        else:
            login(request,user)
            print(redg_no,password)
    else:
        print("no")
        return render(request,"user_profile/login.html")