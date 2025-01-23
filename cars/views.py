from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer
from rest_framework import status
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination

# Create your views here.


class CarListAPIView(APIView):
    def get(self, request):

        cars = Car.objects.all()

        # Sérialiser les données
        serializer = CarSerializer(cars, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

# Voir les voitures filtrées par marque
class BrandCarsAPIView(APIView):

    def get(self, request, brand_id):
        # Vérifier si le token est fourni
        if not request.user.is_authenticated:
            return JsonResponse({'detail': 'Token manquant ou invalide.'}, status=status.HTTP_401_UNAUTHORIZED)

        # Si l'utilisateur est authentifié, on procède avec la logique normale
        cars = Car.objects.filter(brand_id=brand_id)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

class CreateCarAPIView(APIView):

    def post(self, request):
        # Sérialiser les données envoyées
        serializer = CarSerializer(data=request.data)
        
        # Vérifier si les données sont valides
        if serializer.is_valid():
            # Sauvegarder la voiture dans la base de données
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

class CarDeleteAPIView(APIView):

    def delete(self, request, car_id):
        try:
            car = Car.objects.get(id=car_id)
            car.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Car.DoesNotExist:
            return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)

