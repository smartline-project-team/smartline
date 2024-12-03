# serializers.py
from rest_framework import serializers
from .models import Category, Business, Service, Specialist, TimeSlot, Booking

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'price']

class BusinessSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Business
        fields = ['id', 'name', 'description', 'categories']

class SpecialistSerializerMini(serializers.ModelSerializer):
    class Meta:
        model = Specialist
        fields = '__all__'

class BusinessDetailSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    specialists = SpecialistSerializerMini(many=True, read_only=True)

    class Meta:
        model = Business
        fields = ['id', 'name', 'description', 'phone_number', 'email', 'address', 'categories', 'created_at', 'updated_at', 'specialists']

class AvailableTimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ['id', 'date', 'time', 'is_taken']

class SpecialistSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True)
    time_slots = AvailableTimeSlotSerializer(many=True)

    class Meta:
        model = Specialist
        fields = ['id', 'first_name', 'last_name', 'photo', 'services', 'time_slots']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'specialist', 'service', 'time_slot', 'created_at']
