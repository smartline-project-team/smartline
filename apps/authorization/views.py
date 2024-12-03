from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SendVerificationSerializer, ConfirmCodeSerializer

class SendCodeAPIView(GenericAPIView):
    serializer_class = SendVerificationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Код подтверждения отправлен."}, status=status.HTTP_200_OK)

class ConfirmCodeAPIView(GenericAPIView):
    serializer_class = ConfirmCodeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tokens = serializer.save()
        return Response({
            "message": "Подтверждение прошло успешно.",
            "tokens": tokens
        }, status=status.HTTP_200_OK)
