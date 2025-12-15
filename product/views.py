from django.shortcuts import render, get_object_or_404
from rest_framework import status
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

# Create your views here.

class ProductViewSet(ViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ViewProduct(APIView):
    def get(self, request):
        products = Product.objects.select_related('category').all()
        serializer = ProductSerializer(products, many=True, context={'request':request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def view_specific_product(request, id):
    if request.method == 'GET':
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ViewSpecificProduct(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view()
def view_categories(request):
    category = Category.objects.annotate(product_count=Count('products')).all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)

class ViewCategories(APIView):
    def get(self, request):
        category = Category.objects.annotate(product_count=Count('products')).all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

@api_view()
def view_specific_category(request, pk):
    category = get_object_or_404(Category.objects.annotate(product_count=Count('products')), pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)

class ViewSpecificCategory(APIView):
    def get(self, request, pk):
        category = get_object_or_404(Category.objects.annotate(product_count=Count('products')), pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = get_object_or_404(Category.objects.annotate(product_count=Count('products')), pk=pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)