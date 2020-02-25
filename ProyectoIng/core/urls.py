from django.contrib import admin
from django.urls import path
from .views import reg,sidebar,no_sidebar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/',reg.as_view()),
    path('sidebar/',sidebar.as_view()),
    path('nosidebar/',no_sidebar.as_view()),
]
