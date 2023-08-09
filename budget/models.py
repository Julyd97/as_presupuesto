from django.db import models
from user.models import UserBase
from school.models import School
# Create your models here.

class Source(UserBase):
    code = models.CharField(('code'), unique=True, max_length=50)
    name = models.CharField(('name'), max_length=100)

class BudgetItem(UserBase):
    code = models.CharField(('code'), unique=True, max_length=50)
    is_income = models.CharField(('is income'), max_length=200)
    name = models.CharField(('name'), max_length=100)
    parent = models.CharField(('parent'), max_length=100)

class BudgetAccount(UserBase):
    amount = models.FloatField(('amount'))
    id_budget_item = models.ForeignKey(BudgetItem, null=False, on_delete=models.CASCADE)
    id_source = models.ForeignKey(Source, null = False, on_delete=models.CASCADE)