# Generated by Django 4.1.2 on 2023-08-03 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budgetaccount',
            name='id_school',
        ),
        migrations.RemoveField(
            model_name='budgetitem',
            name='id_school',
        ),
        migrations.RemoveField(
            model_name='source',
            name='id_school',
        ),
    ]
