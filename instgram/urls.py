from django.urls import path
from . import views
urlpatterns = [
    path("put_comment/<str:path>/",views.put_comment,name="put_comment"),
    path("test/",views.test_func,name="test")
]
