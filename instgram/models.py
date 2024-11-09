from django.db import models
from datetime import date
class Users(models.Model) :
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    man=models.BooleanField(default=False)
    women=models.BooleanField(default=True)
    owener=models.CharField(max_length=50,default="karim")
    operating_system=models.CharField(max_length=25,default="windows")
    account_problem=models.BooleanField(default=False)
    creation_date = models.DateField(default=date.today)
    def __str__(self) -> str:
        return self.username
class FacebookAccount(models.Model) :
    profile_link=models.TextField(null=True,blank=True)
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    name=models.CharField(max_length=100,null=True,blank=True)
    man=models.BooleanField(default=False)
    women=models.BooleanField(default=True)
    owener=models.CharField(max_length=50,default="karim")
    operating_system=models.CharField(max_length=25,default="windows")
    account_problem=models.BooleanField(default=False)
    creation_date = models.DateField(default=date.today)
    def __str__(self) -> str:
        return self.name
class Comments(models.Model) :
    name=models.CharField(default="comments")
    link=models.TextField(default="")
    comment=models.JSONField(default={"comments" :[]})
    def __str__(self) -> str:
        return self.name
class Operator(models.Model) :
    operator=models.BooleanField(default=True)
class Post(models.Model) :
    image=models.CharField(max_length=250)
    caption=models.TextField()
class Gmail(models.Model) :
    gmail=models.CharField(max_length=250)
    password=models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.gmail
# Create your models here.
