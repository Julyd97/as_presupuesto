# Generated by Django 4.1.2 on 2023-06-28 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_alter_school_institutional_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='institutional_mail',
            field=models.EmailField(max_length=254, null=True, verbose_name='institutional mail'),
        ),
    ]
