from rest_framework import generics
from .models import Category, Business
from .serializers import CategorySerializer, BusinessSerializer, BusinessDetailSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BusinessListAPIView(generics.ListAPIView):
    serializer_class = BusinessSerializer

    def get_queryset(self):
        category = self.request.query_params.get('category', None)
        if category is not None:
            return Business.objects.filter(categories__id=category)
        return Business.objects.all()

class BusinessDetailAPIView(generics.RetrieveAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessDetailSerializer
    lookup_field = 'id'