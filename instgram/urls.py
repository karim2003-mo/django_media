from django.urls import path
from . import views
urlpatterns = [
    path("put_comment/",views.put_comment,name="put_comment"),
    path("test/",views.test_func,name="test"),
    path("delete/",views.delete,name="delete"),
    path("add_comment/",views.add_comment,name="delete"),
    path("add_account/",views.add_account,name="add_account"),
    path("modify_account/",views.modify_account,name="modify_account"),
    path("share_post/",views.posts,name="share_post"),
    path("problem/",views.account_problem,name="problem"),
]
