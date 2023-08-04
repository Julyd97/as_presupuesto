from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, ChangePasswordView, UserView, LogoutView , api_root

urlpatterns = [
    path('', api_root),
    path('login/', TokenObtainPairView.as_view(), name='auth_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='auth_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('users/<int:pk>/', UserView.as_view(), name='auth_user'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    # TODO logout path
]