from django.urls import path
from apps.authorization.views import *

urlpatterns = [
    path('send-code/', SendCodeAPIView.as_view(), name='send-code'),
    path('confirm-code/', ConfirmCodeAPIView.as_view(), name='confirm-code'),
]
