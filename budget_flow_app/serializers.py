from rest_framework import serializers
from django.core.exceptions import ValidationError

from .models import BudgetFlow
from budget.models import BudgetAccount

class BudgetFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = BudgetFlow
        fields = '__all__'
    
    def validate(self, data):
        current_amount_per_month = data.get('amount_per_month')
        user = self.context['request'].user
        id_budget_acccount = data.get('id_budget_account')
        associate_budget_account = BudgetAccount.objects.filter(id = id_budget_acccount.id).first()

        if (sum(current_amount_per_month) > associate_budget_account.amount):
            raise ValidationError('The amount of the budget flow is greater than that of budget account')
        
        return data