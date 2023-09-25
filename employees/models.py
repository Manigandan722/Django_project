from django.db import models

# Create your models here.
class Employees(models.Model):
    First_name=models.CharField(max_length=100)
    Last_name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='images')
    desigination=models.CharField(max_length=100)
    Email=models.EmailField(max_length=100,unique=True)
    phone_number=models.CharField(max_length=12,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    Updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.First_name
    
    
