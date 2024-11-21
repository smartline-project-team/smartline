from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from rest_framework.exceptions import AuthenticationFailed

from .models import EmailConfirmation

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Пароли не совпадают.")
        return data

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password1']

        user = User.objects.create(
            email=email,
            is_active=False  
        )
        user.set_password(password)
        user.save()

        confirmation = EmailConfirmation.objects.create(user=user)

        request = self.context.get('request')
        current_site = get_current_site(request)
        confirmation_url = f"http://{current_site.domain}{reverse('confirm-email', args=[confirmation.token])}"

        send_mail(
            'Подтверждение регистрации',
            f'Привет! Подтверди свою почту по ссылке: {confirmation_url}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False, #при ошибке выведет в консоль причину
        )

        return user
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed('Неверные данные для входа.')
        if not user.is_active:
            raise AuthenticationFailed('Пользователь не активен. Подтвердите email.')

        return {
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'token': user.auth_token.key
        }
