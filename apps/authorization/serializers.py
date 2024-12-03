from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import VerificationCode
from django.core.mail import send_mail
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class SendVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    phone = serializers.CharField(required=False)

    def validate(self, attrs):
        email = attrs.get('email')
        phone = attrs.get('phone')
        if not email and not phone:
            raise serializers.ValidationError("Необходимо указать email или телефон.")
        return attrs

    def save(self):
        email = self.validated_data.get('email')
        phone = self.validated_data.get('phone')
        user, _ = User.objects.get_or_create(email=email)
        verification, _ = VerificationCode.objects.get_or_create(user=user)
        verification.generate_code()

        if email:
            send_mail(
                subject="Ваш код подтверждения",
                message=f"Ваш код подтверждения: {verification.code}",
                from_email="noreply@example.com",  # Укажите ваш email-адрес
                recipient_list=[email],
                fail_silently=False,
            )

class ConfirmCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    phone = serializers.CharField(required=False)
    code = serializers.CharField(max_length=6)

    def validate(self, attrs):
        email = attrs.get('email')
        phone = attrs.get('phone')
        code = attrs.get('code')

        if not email and not phone:
            raise serializers.ValidationError("Необходимо указать email или телефон.")
        
        if not code:
            raise serializers.ValidationError("Необходимо указать код.")

        user = User.objects.filter(email=email).first()
        if not user:
            raise serializers.ValidationError("Пользователь не найден.")
        
        verification = VerificationCode.objects.filter(user=user, code=code, is_used=False).first()
        if not verification:
            raise serializers.ValidationError("Неверный или просроченный код.")

        attrs['user'] = user
        attrs['verification'] = verification
        return attrs

    def save(self):
        user = self.validated_data['user']
        verification = self.validated_data['verification']
        user.is_active = True
        user.save()
        verification.is_used = True
        verification.save()

        # Генерация JWT токенов
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
