from django.db import models

# Create your models here.
class AddData(models.Model):
    sno=models.AutoField(primary_key=True)
    proname=models.CharField(max_length=200)
    prostatus=models.CharField(max_length=40)
    techused=models.CharField(max_length=250)
    prolink=models.CharField(max_length=300)
    gitlink=models.CharField(max_length=300)
    shortdes=models.CharField(max_length=400)
    