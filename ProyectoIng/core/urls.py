from django.contrib import admin
from django.urls import path
from .views import reg,sidebar,no_sidebar,base_barra

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sidebar/',sidebar.as_view(),name='test'),
    path('nosidebar/',no_sidebar.as_view()),
    
]
