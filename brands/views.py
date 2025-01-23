from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Brand
from .serializers import BrandSerializer
from users.permissions import IsAdmin
from rest_framework.pagination import PageNumberPagination


class BrandListAPIView(APIView):
    def get(self, request):

        brands = Brand.objects.all()

        # Sérialiser les données
        serializer = BrandSerializer(brands, many=True)

        # Retourner les données sérialisées
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateBrandAPIView(APIView):

    def post(self, request):
        # Sérialiser les données reçues dans la requête
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            # Sauvegarder la marque dans la base de données
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DeleteBrandAPIView(APIView):

    def delete(self, request, brand_id):
        try:
            brand = Brand.objects.get(id=brand_id)
            brand.delete()
            return Response({'detail': 'Marque supprimée avec succès.'}, status=status.HTTP_204_NO_CONTENT)
        except Brand.DoesNotExist:
            return Response({'detail': 'Marque non trouvée.'}, status=status.HTTP_404_NOT_FOUND)
