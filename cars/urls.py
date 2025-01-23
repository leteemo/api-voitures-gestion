from django.contrib import admin
from django.urls import path
from .views import BrandCarsAPIView, CreateCarAPIView, CarDeleteAPIView, CarListAPIView, UpdateCarAPIView

urlpatterns = [
    path('cars/', CarListAPIView.as_view(), name='car_list'),
    path('cars/<int:car_id>/brand/', BrandCarsAPIView.as_view(), name='car_brand'),
    path('cars/create/', CreateCarAPIView.as_view(), name='car_create'),
    path('cars/delete/<int:car_id>/', CarDeleteAPIView.as_view(), name='care_delete'),
    path('cars/update/<int:car_id>/', UpdateCarAPIView.as_view(), name='update_car'),
]


