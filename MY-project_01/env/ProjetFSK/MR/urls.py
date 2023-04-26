
from django.contrib import admin
from django.urls import path, include
from . import views
from MR.views import (
    singin, singup, dashboard, logout,ForgetPassword,ChangePassword
)
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('Login', singin, name='singin'),
    path('Singup', singup, name='singup'),
    path('Logout', logout, name='logout'),
    path('changepssword',ChangePassword,name='changepassword'),
    path('forgetpassword',ForgetPassword,name='forgetpassword'),
    path('',views.login),
    
]