from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout

# Create your views here.

def myadmin(request):
    alluser = User.objects.all()
    data={'user':alluser}
    return render(request,'sumitadmin/index.html',data)



def mydelete(request,slug):
    print(slug)
    if request.method=="POST":
        myuser = User.objects.get(username=slug)
        myuser.delete()
        return redirect("myadmin")
    else:
        myuser = User.objects.get(username=slug)
        myuser.delete()
        return redirect("myadmin")