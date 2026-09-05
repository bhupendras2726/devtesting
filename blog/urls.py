from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.blogHome, name="blogHome"),
    path("newpost/", views.newPost, name="newPost"),
    path("postcomment", views.postComment, name="postComment"),

    path("<str:slug>", views.blogPost, name="blogPost"),

    
    
]