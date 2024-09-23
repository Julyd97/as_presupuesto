# Generated by Django 3.2.12 on 2024-09-17 16:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('budget', '0005_alter_budgetitem_is_income'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='source',
            options={},
        ),
        migrations.AlterField(
            model_name='source',
            name='code',
            field=models.CharField(max_length=50, verbose_name='code'),
        ),
        migrations.AlterUniqueTogether(
            name='source',
            unique_together={('user_id', 'code')},
        ),
    ]