from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Service(models.Model):
    name = models.CharField(max_length=255) 
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    business = models.ForeignKey('Business', related_name='services', on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.name} - {self.price} сом"

class Business(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name='businesses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

