from turtle import mode
from django.db import models

# Create your models here.
class Studentdetails(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    grade=models.IntegerField()
    url=models.URLField(max_length=100)
    date=models.DateField()
    
    def __str__(self):
        return self.name

