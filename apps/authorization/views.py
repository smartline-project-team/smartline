from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from .serializers import RegistrationSerializer, LoginSerializer
from .models import EmailConfirmation

class RegistrationAPIView(APIView):

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Проверьте свою почту для подтверждения регистрации.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConfirmEmailAPIView(APIView):

    def get(self, request, token):
        confirmation = get_object_or_404(EmailConfirmation, token=token)
        user = confirmation.user
        user.is_active = True
        user.save()
        confirmation.delete()
        return Response({'message': 'Email успешно подтверждён! Теперь вы можете войти.'}, status=status.HTTP_200_OK)

class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data

            user = authenticate(email=user_data['email'], password=request.data['password'])
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                'message': 'Успешный вход в систему.',
                'email': user.email,
                'token': token.key,
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)