from django.urls import path, include
from .views import SourceListCreateAPIView,SourceRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('sources/', SourceListCreateAPIView.as_view(), name='source_list_create'),
    path('sources/<int:pk>/', SourceRetrieveUpdateDestroyAPIView.as_view(), name='source_retrieve_update_destroy')
]