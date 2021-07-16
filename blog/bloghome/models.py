from django.db import models

# Create your models here.

class myusers(models.Model):
    Email     =     models.EmailField(max_length=50,default="")
    userName  =     models.CharField(max_length=30,default="")
    password  =     models.CharField(max_length=30,default="")


    def __str__(self):
        return self.userName


       
class myblogs(models.Model):
    title     =   models.CharField(max_length=100,default="")
    author    =   models.CharField(max_length=30,default="")
    slug      =   models.CharField(max_length=25,default="")
    tags      =   models.CharField(max_length=50,default="")
    contant   =   models.TextField(default="")
    #timestapm      =   models.DateTimeField(blank=True,default="2020-05-03 4:45")

    def __str__(self):
        return self.title