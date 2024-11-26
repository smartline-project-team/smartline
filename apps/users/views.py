from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer, UserDetailSerializer, UserUpdateSerializer

class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]  
    queryset = User.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserDetailSerializer
        return UserUpdateSerializer

    lookup_field = 'email'