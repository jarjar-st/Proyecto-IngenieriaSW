from django.urls import path

from .views import ShowAdsListView

urlpatterns = [
    path('', ShowAdsListView.as_view(), name='my_products'),
]