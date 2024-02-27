from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=200)
    category_image=models.ImageField(upload_to='images',null=True)

    def __str__(self):
        return self.category_name
    
""" If the __str__ method is not there, inside the database, the objects will be shown as model_object_1 instead of its given name! """
    
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=150,null=False,blank=False)
    product_image=models.ImageField(upload_to='images',null=True)
    quantity=models.IntegerField(null=False,blank=False)
    original_price=models.IntegerField(null=False)
    selling_price=models.IntegerField(null=False)
    description=models.TextField(max_length=300,null=False)

    def __str__(self):
        return self.product_name
    

class Cart(models.Model):
    item = models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(null = False, default=1)
    date = models.DateTimeField(auto_now_add = True)