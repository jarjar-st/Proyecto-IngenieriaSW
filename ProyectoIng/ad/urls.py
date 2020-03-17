from django.urls import path

from .views import ShowAdsListView
from .views import AdCreate

urlpatterns = [
    path('', ShowAdsListView.as_view(), name='my_products'),
    path('create/', AdCreate.as_view(), name='create'),
]