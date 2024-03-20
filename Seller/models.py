from django.db import models

# Create your models here.

class Seller(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Add other fields as needed (e.g., address, phone number)

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name=models.CharField(max_length=200)
    category_image=models.ImageField(upload_to='images',null=True)

    def __str__(self):
        return self.category_name
    

class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # Add other fields as needed (e.g., description, image)

    def __str__(self):
        return self.name
