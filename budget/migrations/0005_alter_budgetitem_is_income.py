# Generated by Django 3.2.12 on 2024-09-01 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0004_alter_budgetitem_options_alter_budgetitem_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetitem',
            name='is_income',
            field=models.BooleanField(max_length=200, verbose_name='is income'),
        ),
    ]
