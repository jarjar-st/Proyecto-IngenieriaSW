from django.urls import path
from .views import CreateStore

urlpatterns = [
    path('my_stores',CreateStore.as_view(), name='my_stores'),
]