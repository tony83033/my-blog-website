#from typing_extensions import Required
#from django.http import request, response
from django.shortcuts import redirect, render,HttpResponse
from bloghome.models import myblogs, myusers
from django.contrib import messages
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout
# Create your views here.

def bloghome(request):
    mypost = myblogs.objects.all()
    data = {'post':mypost}
    return render(request,"bloghome/index.html",data)



def mysignup(request):
    if request.method=="POST":
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if len(username)>20:
            messages.warning(request,"username cannot be more than 20 char")
            return redirect("/")

        if len(username)<5:
            messages.warning(request,"username cannot be less than 5 char")
            return  redirect("/")

       

        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already taken")
            
            return redirect("/")

        if len(password)<5:
            messages.warning(request,"Password cannot be less than 5 char")
            return redirect("/")

        if len(password)>20:
            messages.warning(request,"Password cannot be more than 20 char")
            return redirect("/")

        if password!=cpassword:
            messages.warning(request,"Confirm password and password not match")
            return redirect("/")
       

        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already exists! try logging in")
            return redirect("/")

        

        print(email,username,password)

        myuser = myusers(Email=email,userName=username,password=password)

        myuser.save()

        cuser = User.objects.create_user(username, email, password)
        cuser.save()
        user=authenticate(username=username,password=password)
        login(request,user)
        messages.success(request,"Welcome "+username)
        return redirect("/")
    return HttpResponse("404 Not Found")
        

def mylogin(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        if len(username)<5:
             messages.error(request,"Invalid credentials! Please try again")
             return redirect("/")

        if len(password)<5:
             messages.error(request,"Invalid credentials! Please try again")
             return redirect("/")


        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"Welcome "+username)
            return redirect("/")
        else:
            messages.error(request,"Invalid credentials! Please try again")
            return redirect("/")
    return HttpResponse("404 Not Found")

def mylogout(request):

    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect("/")

def blogpage(request,slug):
    post = myblogs.objects.filter(slug=slug)
    context={'post':post}

    return render(request,"bloghome/blog.html",context)




