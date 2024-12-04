from django.shortcuts import render
from django.db.models.deletion import ProtectedError
from django.db import IntegrityError
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response


from .models import Source, BudgetItem, BudgetAccount
from .serializers import SourceSerializer, BudgetItemSerializer, BudgetAccountSerializer
from .exceptions import ItemProtected
from user.permissions import IsOwner
            
class SourceListCreateAPIView(ListCreateAPIView):
    queryset =Source.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)
    serializer_class = SourceSerializer

    def get_queryset(self):
        user = self.request.user
        return Source.objects.filter(user = user)
    
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def post(self, request):
        serializer = SourceSerializer(data = request.data, context={'request': request})
        if serializer.is_valid():
            try:
                serializer.save(user=self.request.user)  # Save the new item
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError:
                return Response('The source already exist.', status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SourceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Source.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)
    serializer_class = SourceSerializer
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': f'{str(request)} has been deleted.'})

class BudgetItemListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BudgetItemSerializer
    queryset = BudgetItem.objects.all()

    def get_queryset(self):
        user = self.request.user
        return BudgetItem.objects.filter(user = user).order_by('code')
    
    def post(self, request):
        serializer = BudgetItemSerializer(data = request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=self.request.user)  # Save the new item
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BudgetItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BudgetItemSerializer
    queryset = BudgetItem.objects.all()
    lookup_field = 'pk'

    def destroy(self, request, *args, **kwargs):
        """
        Override default method. Check if item is protected
        """
        instance = self.get_object()
        print(instance.id)
        associate_budget_account = BudgetAccount.objects.filter(id_budget_item = instance.id).first()
        if associate_budget_account != None:
            raise ItemProtected()
        try:
            self.perform_destroy(instance)
            data = {'message': 'The item was deleted successful'}
        except ProtectedError:
            raise ItemProtected()
        return Response(data,status=status.HTTP_200_OK)

class BudgetAccountListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BudgetAccountSerializer
    queryset = BudgetAccount.objects.all()

    def get_queryset(self):
        user = self.request.user
        return BudgetAccount.objects.filter(user = user)
    
    def post(self, request):
        serializer = BudgetAccountSerializer(data = request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(user=self.request.user)  # Save the new item
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class BudgetAccountRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BudgetAccountSerializer
    queryset = BudgetAccount.objects.all()
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
        
    