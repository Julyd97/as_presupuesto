from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError


from user.models import UserBase
from budget.models import BudgetAccount


def validate_array_floats(value):
        if any(num <= 0 for num in value):
            raise ValidationError('All values in the array must be positive numbers.')
        elif (len(value) < 12):
             raise ValidationError("Amount per month must be a list of length equal to the number of months")

class BudgetFlow(UserBase):
    id_budget_account = models.ForeignKey(BudgetAccount, null=False, on_delete=models.CASCADE)
    amount_per_month = ArrayField(models.FloatField(), validators=[validate_array_floats],null =True, size = 12)
