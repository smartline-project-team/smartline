from django.urls import path
from .views import RegistrationAPIView, ConfirmEmailAPIView, LoginAPIView, ResendEmailAPIView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('confirm-email/<uuid:token>/', ConfirmEmailAPIView.as_view(), name='confirm-email'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('resend-email/', ResendEmailAPIView.as_view(), name='resend-email'),  
]
