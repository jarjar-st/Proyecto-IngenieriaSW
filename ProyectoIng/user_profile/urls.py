from django.urls import path
from .views import AccountUpdate


urlpatterns = [
    path('', AccountUpdate.as_view(), name="profileconf")
]