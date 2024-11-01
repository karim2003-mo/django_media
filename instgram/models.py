from django.db import models
class Users(models.Model) :
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.username
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
# Create your models here.
