from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index' ),
    # path('about', views.about, name='about' ),
    path('register', views.user_register, name='register' ),
    path('login', views.user_login, name='login' ),
    path('logout', views.user_logout, name='logout' ),
    path('post_blog', views.post_blog, name='post_blog' ),
    path('blog_detail/<int:id>', views.blog_detail, name='blog_detail' ),
    path('delete/<int:id>', views.delete, name='delete' ),
    path('edite/<int:id>', views.edite, name='edite' ),
]