# file: backend/urls.py
from django.conf.urls import url, include
from django.urls import path
from api.views import home,problem,post,editpost,logged,user,about
from api.resources import UsersResource

# handling resources
UsersResource = UsersResource()

urlpatterns = [
    path("",home),
    path("home/",home),
    path("problem/",problem),
    path("post/",post),
    path("edit-post/",editpost),
    path("logged/",logged),
    path("user/",user),
    path("about/",about),
]