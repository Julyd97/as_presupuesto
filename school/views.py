from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.
from .models import School
from .serializers import SchoolSerializer
from user.permissions import IsOwner

class SchoolView(generics.RetrieveUpdateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = (IsAuthenticated, IsOwner)

@api_view(['GET'])
def api_root(request, format = None):
    return Response({
        'schools': reverse('school-list', request=request, format=format,args=['0']),
        })