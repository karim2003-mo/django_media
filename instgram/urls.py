from django.urls import path
from . import views
urlpatterns = [
    path("put_comment/",views.put_comment,name="put_comment"),
]
