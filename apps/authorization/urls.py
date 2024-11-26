from django.urls import path
from .views import RegistrationAPIView, ConfirmEmailAPIView, LoginAPIView, ResendEmailAPIView, LogoutApiView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('confirm-email/<uuid:token>/', ConfirmEmailAPIView.as_view(), name='confirm-email'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('resend-email/', ResendEmailAPIView.as_view(), name='resend-email'),  
    path('logout/', LogoutApiView.as_view(), name='logout_api'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
