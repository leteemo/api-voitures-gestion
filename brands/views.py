from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Brand
from .serializers import BrandSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAdmin
from rest_framework.pagination import PageNumberPagination


class BrandListAPIView(APIView):
    def get(self, request):

        brands = Brand.objects.all()

        # Initialiser la pagination
        paginator = PageNumberPagination()
        
        # Permettre la personnalisation de la limite via un paramètre `limit`
        paginator.page_size = request.query_params.get('limit', 10)

        # Paginer les résultats
        result_page = paginator.paginate_queryset(brands, request)

        serializer = BrandSerializer(result_page, many=True)

        # Retourner une réponse paginée
        return paginator.get_paginated_response(serializer.data)

class CreateBrandAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmin]

    def post(self, request):
        # Sérialiser les données reçues dans la requête
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            # Sauvegarder la marque dans la base de données
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class DeleteBrandAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmin]

    def delete(self, request, brand_id):
        try:
            brand = Brand.objects.get(id=brand_id)
            brand.delete()
            return Response({'detail': 'Marque supprimée avec succès.'}, status=status.HTTP_204_NO_CONTENT)
        except Brand.DoesNotExist:
            return Response({'detail': 'Marque non trouvée.'}, status=status.HTTP_404_NOT_FOUND)

class UpdateBrandAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmin]

    def put(self, request, brand_id):
        try:
            brand = Brand.objects.get(id=brand_id)  # Récupérer la marque à modifier
        except Brand.DoesNotExist:
            return Response({"error": "Brand not found."}, status=status.HTTP_404_NOT_FOUND)

        # Sérialiser et valider les données
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, brand_id):
        try:
            brand = Brand.objects.get(id=brand_id)  # Récupérer la marque à modifier
        except Brand.DoesNotExist:
            return Response({"error": "Brand not found."}, status=status.HTTP_404_NOT_FOUND)

        # Sérialiser et valider les données partiellement
        serializer = BrandSerializer(brand, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)