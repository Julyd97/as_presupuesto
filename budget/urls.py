from django.urls import path, include
from .views import SourceListCreateAPIView,SourceRetrieveUpdateDestroyAPIView, BudgetItemListCreateAPIView, BudgetItemRetrieveUpdateDestroyAPIView, BudgetAccountListCreateAPIView, BudgetAccountRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('sources/', SourceListCreateAPIView.as_view(), name='source_list_create'),
    path('sources/<int:pk>/', SourceRetrieveUpdateDestroyAPIView.as_view(), name='source_retrieve_update_destroy'),
    path('budgetitems/', BudgetItemListCreateAPIView.as_view(), name='budgetitem_list_create'),
    path('budgetitems/<int:pk>/', BudgetItemRetrieveUpdateDestroyAPIView.as_view(), name='budgetitem_retrieve_update_destroy'),
    path('budgetaccounts/', BudgetAccountListCreateAPIView.as_view(), name = 'budgetaccount_list_create'),
    path('budgetaccounts/<int:pk>/', BudgetAccountRetrieveUpdateDestroyAPIView.as_view(), name='budgetaccount_retrieve_update_destroy')
]