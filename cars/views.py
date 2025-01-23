from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination

# Create your views here.


class CarListAPIView(APIView):
    def get(self, request):
        cars = Car.objects.all()

        paginator = PageNumberPagination()
        paginator.page_size = request.query_params.get('limit', 10)

        result_page = paginator.paginate_queryset(cars, request)

        serializer = CarSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)

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
    authentication_classes = [JWTAuthentication]

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
    authentication_classes = [JWTAuthentication]

    def delete(self, request, car_id):
        try:
            car = Car.objects.get(id=car_id)
            car.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Car.DoesNotExist:
            return Response({"error": "Car not found"}, status=status.HTTP_404_NOT_FOUND)


class UpdateCarAPIView(APIView):

    authentication_classes = [JWTAuthentication]

    def put(self, request, car_id):
        try:
            car = Car.objects.get(id=car_id)  # Récupérer la voiture à modifier
        except Car.DoesNotExist:
            return Response({"error": "Car not found."}, status=status.HTTP_404_NOT_FOUND)

        # Sérialiser et valider les données
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, car_id):
        try:
            car = Car.objects.get(id=car_id)  # Récupérer la voiture à modifier
        except Car.DoesNotExist:
            return Response({"error": "Car not found."}, status=status.HTTP_404_NOT_FOUND)

        # Sérialiser et valider les données partiellement
        serializer = CarSerializer(car, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)