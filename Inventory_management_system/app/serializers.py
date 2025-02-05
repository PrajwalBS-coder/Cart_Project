# from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *
from .validators import *
class SellerSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        email=serializers.EmailField(validators=[Email_Validators])
class ProductSerailizer(serializers.ModelSerializer):
    supplier=serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())
    class Meta:
        model = Product
        fields = ['name','description','catepory','price','stock_quantity','supplier']
