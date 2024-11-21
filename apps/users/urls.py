from django.urls import path
from .views import UserListAPIView, UserDetailAPIView

urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('users/<str:email>/', UserDetailAPIView.as_view(), name='user-detail'),
]
