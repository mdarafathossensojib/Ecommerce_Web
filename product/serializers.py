from rest_framework import serializers
from decimal import Decimal
from product.models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'product_count']
    product_count = serializers.IntegerField()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'price_with_tax', 'category', 'stock']

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product):
        return round(product.price * Decimal(1.1), 2)
    
    def validate_price(self, price):
        if price < 0:
            raise serializers.ValidationError("Price must be a positive number.")
        
        return price
    
