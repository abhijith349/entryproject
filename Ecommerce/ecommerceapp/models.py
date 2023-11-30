from django.db import models

# Create your models here.
class product(models.Model):
    name= models.CharField(max_length=20)
    price= models.CharField(max_length=10)
    brand= models.CharField(max_length=20)
    description= models.CharField(max_length=100)