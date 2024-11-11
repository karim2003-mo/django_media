from django.shortcuts import render
from django.http import JsonResponse
from .models import *
def test(request) :
    users = Users.objects.all()
    l=[]
    for user in users :
        l.append(user.username)
    return JsonResponse({"result":l})
# Create your views here.
