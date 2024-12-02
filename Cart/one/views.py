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

def Edit(request):
    uname=request.session.get('username')
    UserObj=User.objects.filter(name=uname)
    # if request.method=='POST':
    #     newname=request.POST['name']
    #     newemail=request.POST['email']
    #     newimg=request.FILES['profileImage']
    #     UpdateUser=User.objects.filter(name=uname)
    #     # User.objects.update(name=newname,email=newemail,profile_image=newimg)
    #     UpdateUser[0].name=newname
    #     UpdateUser[0].email=newemail
    #     UpdateUser[0].profile_img=newimg
    #     UpdateUser[0].save()
    UpdateUser=User.objects.none()
    if request.method == 'POST':
        newname = request.POST.get('name')
        newemail = request.POST.get('email')
        newimg = request.FILES.get('profileImage')
        UpdateUser = User.objects.filter(name=uname).first()
        print(UpdateUser,newimg)

        if UpdateUser:
            if newname:
                UpdateUser.name = newname
            if newemail:
                UpdateUser.email = newemail
            if newimg:
                UpdateUser.profile_image = newimg
            UpdateUser.save()
            return render(request,'Profile.html',{'user':User.objects.filter(name=newname)[0]})

        else:
            # Handle the case where the user isn't found
            print("User not found")


    return render(request,'Edit.html',{'user':UserObj[0]})


def UserProfile(request):
    uname=request.session.get('username')
    UserObj=User.objects.filter(name=uname)
    return render(request,'Profile.html',{'user':UserObj[0]})
    

def ForgotPassword(request):
    if request.method=='POST':
        username=request.POST.get('username')
        UserObj=User.objects.filter(name=username).first()
        print(UserObj)
        if UserObj:
            UserObj.password=request.POST['password']
            UserObj.save()
            return HttpResponseRedirect(reverse('userLogin'))
        else:
            return render(request,'ForgotPassword.html')
    return render(request,'ForgotPassword.html')
    

def ResetPassword(request):
    name=request.session['username']
    if request.method=='POST':
        UserObj=User.objects.filter(name=name).first()
        if (request.POST['password']==request.POST['confirmpassword']):
            UserObj.password=request.POST['password']
            UserObj.save()
            UserLogout(request)
            return HttpResponseRedirect(reverse('Home'))

    else:
        return render(request,'ResetPassword.html')


def AddToCart(request):
    if request.session.get('username'):
        if request.method=="POST":
            username=request.session.get('username')
            print("Added To Cart By ",username,request.POST['productname'])
            obj= Cart.objects.get_or_create(product_name=request.POST.get('productname'),customer_name=username,price=request.POST.get('price'),product_count=1)
            if obj:
                return HttpResponseRedirect(reverse('Home'))
            else:
                return HttpResponse("error")
        # return HttpResponseRedirect(reverse('profile'))
    return HttpResponseRedirect(reverse('userLogin'))
