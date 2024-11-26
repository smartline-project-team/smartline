from django.urls import path
from .views import UserListAPIView, UserDetailUpdateAPIView

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-list'),
    path('users/<str:email>/', UserDetailUpdateAPIView.as_view(), name='user-detail-update'),
]
