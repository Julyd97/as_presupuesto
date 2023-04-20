from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import User
from .serializers import RegisterSerializer, ChangePasswordSerializer, UserSerializer
from .permissions import IsSameUser


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsSameUser,)
    serializer_class = ChangePasswordSerializer

class UserView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsSameUser,)
    serializer_class = UserSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'login': reverse('auth_obtain_pair', request=request, format=format),
        'refresh': reverse('auth_refresh', request=request, format=format),
        'register': reverse('auth_register', request=request, format=format),
        'change_password': reverse('auth_change_password', request=request, format=format, args=['1']),
        'user': reverse('auth_user', request=request, format=format, args=['1']),
    })