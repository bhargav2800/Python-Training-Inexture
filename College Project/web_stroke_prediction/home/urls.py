from django import views
from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name="home"),
    path('login',views.loginuser,name="loginuser"),
    path('register',views.register,name='register'),
    path('stroke_predict',views.stroke_predict,name='stroke_predict')
]