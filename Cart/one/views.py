from django.shortcuts import render
from django.http import *
from .models import *
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def AddUser(request):
    if request.method=='POST':
        if(request.POST['password']==request.POST['confirm-password']):
            obj=User.objects.get_or_create(name=request.POST['name'],email=request.POST['email'],password=request.POST['password'])
            if obj:
                return HttpResponseRedirect(reverse('Home'))
        else:
            return render(request,'Registration.html')
    return render(request,'Registration.html')

def home(request):
    if request.session.get('username'):
        return render(request,'HomePage.html',{'name':request.session.get('username')})
    return render(request,'HomePage.html')

def UserLogin(request):
    if request.method=='POST':
        na=request.POST['username']
        paswd=request.POST['password']
        # AuthObj=authenticate(username=na,password=paswd)
        # print(AuthObj)
        # if  AuthObj:
        #     if AuthObj.is_active:
        #         login(request,AuthObj)
        #         request.session['username']=request.POST['username']
        #         return HttpResponseRedirect(reverse('Home'))
        #     else:
        #         return HttpResponse("Your Account Experied Please Renew!!")
        # else:
            # return HttpResponse("You've Not Created The Account Please Create The Account And Continue😎")
        AuthObj=User.objects.filter(name=na,password=paswd)
        if AuthObj:
            # login(request,AuthObj)
            request.session['username']=request.POST['username']
            request.session['is_logged_in'] = True
            return HttpResponseRedirect(reverse('Home'))
    return render(request,'UserLogin.html')

def UserLogout(request):
    request.session['is_logged_in'] = False
    request.session.clear()
    return HttpResponseRedirect(reverse('Home'))
    