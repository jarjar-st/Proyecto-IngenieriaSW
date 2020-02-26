from django.urls import path
from .views import CreateUser,TemplateLogin

urlpatterns = [
    path('signup',CreateUser.as_view(), name='signup'),
    path('signup',TemplateLogin.as_view(), name='login'),
]