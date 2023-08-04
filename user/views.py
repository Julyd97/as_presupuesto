from rest_framework import generics, status
from rest_framework.views import APIView 
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import User, BlacklistedRefreshToken
from .serializers import RegisterSerializer, ChangePasswordSerializer, UserSerializer
from .permissions import IsSameUser

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        serializer.save()
        # cual es el user creado
        # crear school


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsSameUser,)
    serializer_class = ChangePasswordSerializer


class UserView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, IsSameUser,)
    serializer_class = UserSerializer

class LogoutView(APIView):
    permission_classes = (IsAuthenticated, IsSameUser)

    def post(self, request):
        refresh_token = request.data.get("refresh_token", None)
        print(refresh_token)
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                print(token.verify())
                token.blacklist()
                # Also add the RefreshToken to the blacklist
                BlacklistedRefreshToken.objects.create(token=refresh_token)
                return Response({"detail": "Logout successful"}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"detail": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({"detail": "Refresh token not provided"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'login': reverse('auth_obtain_pair', request=request, format=format),
        'refresh': reverse('auth_refresh', request=request, format=format),
        'register': reverse('auth_register', request=request, format=format),
        'change_password': reverse('auth_change_password', request=request, format=format, args=['0']),
        'user': reverse('auth_user', request=request, format=format, args=['0']),
    })