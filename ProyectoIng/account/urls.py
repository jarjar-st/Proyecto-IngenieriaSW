from django.urls import path
from .views import CreateUser,TemplateLogin,logout_view

urlpatterns = [
    path('signup',CreateUser.as_view(), name='signup'),#Template Registro
    path('login',TemplateLogin.as_view(), name='login'),#Template Login
    path('logout',logout_view, name='logout'),#Logout
]