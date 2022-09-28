from django.db import models

# Create your models here.
class feature(models.Model):
    Name = models.CharField(max_length=200)
    Age= models.CharField(max_length=20)