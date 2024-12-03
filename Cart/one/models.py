from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    profile_image = models.ImageField(blank=True, default='static/images/profile.jpg')
    def __str__(self):
        return (self.name)

class Cart(models.Model):
    product_name=models.CharField(max_length=100)
    customer_name=models.CharField(max_length=100)
    price=models.IntegerField()
    product_count=models.IntegerField()
    def __str__(self):
        return (self.product_name)