from django.contrib import admin
from django.urls import path
from .views import BrandListAPIView, CreateBrandAPIView, DeleteBrandAPIView, UpdateBrandAPIView

urlpatterns = [
    path('brands/', BrandListAPIView.as_view(), name='brands'),
    path('brands/create/', CreateBrandAPIView.as_view(), name='create_brand'),  # Créer une marque
    path('brands/delete/<int:brand_id>/', DeleteBrandAPIView.as_view(), name='delete_brand'), 
]