from django.urls import path
from .views import *
urlpatterns=[
    path('Add-suppliers',Supplier_View.as_view(),name='suppliers'),
    path('Add-Product/',Product_View.as_view(),name='Product_add')
]