from django.shortcuts import render
from django.db.models.deletion import ProtectedError
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import BudgetFlow
from .serializers import BudgetFlowSerializer
from .exceptions import ItemProtected

class BudgetFLowCreateAPIView(ListCreateAPIView):
    queryset = BudgetFlow.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BudgetFlowSerializer

    def get_queryset(self):
        user = self.request.user
        return BudgetFlow.objects.all(user = user)
    
    def post(self, request):
        serializer = BudgetFlowSerializer(data = request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=self.request.user)  # Save the new item
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BudgetFlowRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BudgetFlow.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = BudgetFlowSerializer
    lookup_field = 'pk'

    def destroy(self, request, *args, **kwargs):
        """
        Override default method. Check if item is protected
        """
        instance = self.get_object()
        try:
            self.perform_destroy(instance)
            data = {'message': 'The item was deleted successful'}
        except ProtectedError:
            raise ItemProtected()
        return Response(data,status=status.HTTP_200_OK)
# Create your views here.
