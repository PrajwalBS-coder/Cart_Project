from django.shortcuts import render
from django.http import *
from .models import *
from django.urls import reverse
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
