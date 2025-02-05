from django.db import models

# Create your models here.
class Supplier(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    phone=models.CharField(max_length=100,unique=True)
    address=models.CharField(max_length=100)
    class Meta:
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"

class Product(models.Model):
    name = models.CharField(max_length=255,unique=True)
    description=models.TextField(max_length=300)
    catepory=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock_quantity=models.IntegerField()
    supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

class Sale_Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    movement_type=models.CharField(max_length=100,choices=(('In','In'),('Out','Out')))
    movement_date=models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = "Sale Order"
        verbose_name_plural = "Sale Orders"

class Stock_Movement(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    movement_type=models.CharField(max_length=100,choices=(('In','In'),('Out','Out')))
    movement_date=models.DateField(auto_now_add=True)
    notes=models.TextField(max_length=300)
    class Meta:
        verbose_name = "Stock Movement"
        verbose_name_plural = "Stock Movements"



