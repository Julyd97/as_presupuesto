from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Source
from .serializers import SourceSerializer
from user.permissions import IsOwner

# Create your views here.
# class SourceView(APIView):
#     model = Source
#     permission_classes = (IsAuthenticated, IsOwner)

#     def get(self, request, pk=None, format=None):
#         if pk is not None:
#             source = Source.model.objects.get(id=pk).first()
#             if not source:
#                 return Response({"detail": "Source not found."}, status=status.HTTP_404_NOT_FOUND)
#             serializer = SourceSerializer(source)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             sources = Source.objects.all()
#             serializer = SourceSerializer(sources, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
            
class SourceListCreateAPIView(ListCreateAPIView):
    queryset =Source.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)
    serializer_class = SourceSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SourceRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Source.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)
    serializer_class = SourceSerializer
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': f'{str(request)} has been deleted.'})

# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Item  # Replace 'Item' with your model name
# from .serializers import ItemSerializer  # Replace with your serializer

#  class ItemListCreateAPIView(ListCreateAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer

# class ItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#     lookup_field = 'pk'  # Replace 'pk' with the field used for item ID in the URL

#     def delete(self, request, *args, **kwargs):
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response({"detail": "Item deleted successfully."}, status=status.HTTP_204_NO_CONTENT)