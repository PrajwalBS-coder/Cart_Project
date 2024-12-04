"""
URL configuration for Cart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import *
from one.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Checking/',TemplateView.as_view(template_name='AllInONe.html'),name='Check'),
    # path('home/',TemplateView.as_view(template_name='HomePage.html'),name='Home'),
    path('home/',home,name='Home'),
    path('registration/',AddUser,name='registration'),
    path('userlogin/',UserLogin,name='userLogin'),
    path('userLogout/',UserLogout,name='userLogout'),
    path('UserProfile/',UserProfile,name='profile'),
    path('UserProfileEdit/',Edit,name='edit'),
    path('forgotpassword/',ForgotPassword,name='forgotpassword'),
    path('resetpassword/',ResetPassword,name='resetpassword'),
    path('addtocart/',AddToCart,name='addtocart'),
    path('cart/',UserCart,name='cart'),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
