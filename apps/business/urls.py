from django.urls import path
from .views import CategoryListAPIView, BusinessDetailAPIView, BusinessListAPIView


urlpatterns = [
    path('', BusinessListAPIView.as_view(), name='business-list'),
    path('<int:id>/', BusinessDetailAPIView.as_view(), name='business-detail'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
]
