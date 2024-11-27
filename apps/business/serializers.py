# serializers.py
from rest_framework import serializers
from .models import Category, Business, Service

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'price']

class BusinessSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    
    class Meta:
        model = Business
        fields = ['id', 'name', 'description', 'categories']

class BusinessDetailSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    services = ServiceSerializer(many=True)

    class Meta:
        model = Business
        fields = ['id', 'name', 'description', 'phone_number', 'email', 'address', 'categories', 'created_at', 'updated_at', 'services']
