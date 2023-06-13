from django.db import models

class pagecategry(models.Model):
    name=models.CharField(max_length=100)
    notes=models.TextField(blank=True,null=True)
# Create your models here.
class page(models.Model):
    name=models.CharField(max_length=100)
    Date=models.DateField()
class Gowtham(models.Model):
    name=models.CharField(max_length=20)
    rollno=models.IntegerField(max_length=50)
    contect=models.IntegerField(max_length=50)
    city=models.CharField(max_length=50)





