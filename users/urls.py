from django.urls import path
from .views import UserRegisterAPIView

urlpatterns = [
    path('users/register/', UserRegisterAPIView.as_view(), name='register'),
]