# Generated by Django 4.1.2 on 2023-05-20 01:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('dane_code', models.CharField(max_length=100, unique=True, verbose_name='dane code')),
                ('cont_menor_cuantia', models.CharField(blank=True, max_length=30, verbose_name='contratacion menor cuantia')),
                ('cont_minima_cuantia', models.CharField(blank=True, max_length=30, verbose_name='contratacion minima cuantia')),
                ('institutional_mail', models.EmailField(max_length=254, unique=True, verbose_name='institutional mail')),
                ('address', models.CharField(max_length=30, verbose_name='address')),
                ('date_acuerdos', models.DateField(blank=True, verbose_name='date acuerdos')),
                ('date_resolucion', models.DateField(blank=True, verbose_name='date resolucion')),
                ('lema', models.CharField(max_length=120, verbose_name='lema')),
                ('localidad', models.CharField(max_length=20, verbose_name='localidad')),
                ('cellphone', models.IntegerField(verbose_name='cellphone')),
                ('phone', models.IntegerField(verbose_name='phone')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
                'abstract': False,
            },
        ),
    ]
