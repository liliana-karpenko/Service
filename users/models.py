from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.contrib.auth.models import User, Group


class User(AbstractUser):
    pass

class Customer(models.Model):
    Name = models.CharField('Name Customer', max_length=100)
    Email = models.EmailField('Email Customer', max_length = 254)
    phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    Phone = models.CharField('Phone Customer', validators = [phoneNumberRegex], max_length = 16, unique = True)
    Address = models.CharField('Address Customer', max_length = 100)
    Birthdate = models.DateField('Birthdate Customer')

    def __str__(self):
        return self.Name

class Car(models.Model):
    owner = models.ForeignKey(Customer, on_delete = models.CASCADE) #on_delete = models.CASCADE при удалении статьи удаляться и комменты
    manufacturer = models.CharField('Manufacturer', max_length = 50)
    model = models.CharField('Model', max_length = 100)
    yearOfManufacture = models.IntegerField('Year of manufacture')

    def __str__(self):
        return self.manufacturer

class Order(models.Model):
    car = models.ForeignKey(Car, on_delete = models.CASCADE)
    user = models.CharField('Name user', max_length = 50)
    date = models.DateField('Name Customer', auto_now_add = True)
    amount = models.DecimalField('Amount($)', max_digits = 11, decimal_places = 5)
    for_status = (
        ('process', 'process'),
        ('done', 'done'),
    )
    status = models.CharField(max_length=7, choices=for_status, default='unknown')





