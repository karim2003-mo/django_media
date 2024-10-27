from django.db import models
class Users(models.Model) :
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.username
class Comments(models.Model) :
    comment=models.TextField()
    def __str__(self) -> str:
        return self.comment
# Create your models here.
