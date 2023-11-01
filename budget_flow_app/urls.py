from django.urls import path, include
from .views import BudgetFLowCreateAPIView, BudgetFlowRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('flow/', BudgetFLowCreateAPIView.as_view(), name='budgetflow_list_create'),
    path('flow/<int:pk>/', BudgetFlowRetrieveUpdateDestroyAPIView.as_view(), name='budgetflow_retrieve_update_destroy'),
]