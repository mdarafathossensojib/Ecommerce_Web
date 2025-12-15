from django.shortcuts import render, get_object_or_404
from rest_framework import status
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()
        if product.stock > 10:
            return Response({"message": "Cannot delete product with stock greater than 10."}, status=status.HTTP_400_BAD_REQUEST)
        self.product.perform_destroy()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializer
  

    def destroy(self, request, *args, **kwargs):
        category = self.get_object()
        if category.products.exists():
            return Response({"message": "Cannot delete category with associated products."}, status=status.HTTP_400_BAD_REQUEST)
        category.perform_destroy()
        return Response(status=status.HTTP_204_NO_CONTENT)