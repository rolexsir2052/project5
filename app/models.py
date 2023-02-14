from django.db import models

# Create your models here.
class Client(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Phone=models.IntegerField()
    