from rest_framework import serializers
from django.core.exceptions import ValidationError
from rest_framework.fields import CurrentUserDefault
from .models import *

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ['code', 'name','user']

class BudgetItemSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = BudgetItem
        fields = '__all__'

    def update(self, instance, validated_data):
        # Exclude changes to the 'parent and is_income' field
        if 'parent' in validated_data:
            validated_data.pop('parent')
        elif 'is_income' in validated_data:
            validated_data.pop('is_income')
        return super().update(instance, validated_data)
    
    def validate(self, data):
        id_parent = data.get('parent')
        user = self.context['request'].user
        associate_budget_account = BudgetAccount.objects.filter(id_budget_item = id_parent).first()
        print(associate_budget_account)
        if id_parent != None:
            parentBudgetItem = BudgetItem.objects.filter(id = id_parent.id, user = user).first()
            print(parentBudgetItem.is_income)
            
            if parentBudgetItem == None:
                raise ValidationError("Parent item not found")
            
            data['is_income'] = parentBudgetItem.is_income
        if associate_budget_account != None:
            raise ValidationError("Parent item already have a budget account associate and cant have childs")
        return data
        
        

class BudgetAccountSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = BudgetAccount
        fields = '__all__'

    def update(self, instance, validated_data):
        if 'id_budget_item' in validated_data:
            validated_data.pop('id_budget_item')
        elif 'id_source' in validated_data:
            validated_data.pop('id_source')
        return super().update(instance, validated_data)

    def validate(self,data):
        id_budget_item = data.get('id_budget_item')
        id_source = data.get('id_source')
        user = self.context['request'].user
        budget_item_itsparent = BudgetItem.objects.filter(parent = id_budget_item).first()
        if budget_item_itsparent != None:
            raise ValidationError('The budget item its a parent')
        current_budget_item = BudgetItem.objects.filter(id = id_budget_item.id, user = user).first() 
        current_source = Source.objects.filter(id = id_source.id, user = user).first()
        new_budgetaccount = BudgetAccount.objects.filter(id_budget_item = current_budget_item).first()
        print(current_budget_item)
        print(current_source)
        if current_budget_item!=None and current_source!=None :
            if current_budget_item.is_income == True and new_budgetaccount != None:
                raise ValidationError('The budget item already had a budget account') # budget items its an income so must have just 1 budget account
        return data