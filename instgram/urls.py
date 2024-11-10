from django.urls import path
from .views import SocialInstgram
social= SocialInstgram()
urlpatterns = [
    path("put_comment/",social.comment_only,name="put_comment"),
    path("comment_and_react/",social.comment_and_react,name="comment_and_react"),
    path("react_only/",social.react_only,name="react_only"),
    path("test/",social.test_func,name="test"),
    path("delete/",social.delete,name="delete"),
    path("add_comment/",social.add_comment,name="delete"),
    path("add_account/",social.add_account,name="add_account"),
    path("modify_account/",social.modify_account,name="modify_account"),
    path("share_post/",social.posts,name="share_post"),
    path("problem/",social.account_problem,name="problem"),
]
