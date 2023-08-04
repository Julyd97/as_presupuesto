from rest_framework import serializers
from .models import *

class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source
        fields = ['code','name']

class BudgetItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BudgetItem
        fields = '__all__'

class BudgetAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BudgetAccount
        fields = '__all__'