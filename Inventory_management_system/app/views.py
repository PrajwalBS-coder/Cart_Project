from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response



class Supplier_View(APIView):
    def post(self,request):
        serailzers=SellerSerailizer(data=request.data)
        if serailzers.is_valid():
            serailzers.save()
            return Response({"message": "Supplier created successfully"}, status=201)
        return Response({"message": "Invalid data"}, status=400)

class Product_View(APIView):
    def post(self, request):
        serailzers=ProductSerailizer(data=request.data)
        if serailzers.is_valid():
            serailzers.save()
            return Response({"message": "Supplier created successfully"}, status=201)
        return Response({"message": "Invalid data"}, status=400)
        

