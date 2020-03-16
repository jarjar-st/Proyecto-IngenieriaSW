from django.urls import path,include
from .views import main_page,CategoryDetailView

urlpatterns = [
    path('', main_page.as_view(), name="home"),
    path('category/<int:pk>', CategoryDetailView.as_view(), name="category_products"),
   
]


