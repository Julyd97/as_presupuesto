from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SchoolView, api_root
urlpatterns = [
    path('', api_root),
    path('detail/<int:pk>/', SchoolView.as_view(), name = 'school-update')
    ]