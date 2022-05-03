from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Customer(models.Model):
    Name = models.CharField('Name Customer', max_length=100)
    EmailRegex = RegexValidator(regex=r"^[-\w.]+@([A-z0-9][-A-z0-9]+\.)+[A-z]{2,4}$")
    Email = models.EmailField('Email Customer', validators=[EmailRegex], max_length=254, unique=True)
    PhoneNumberRegex = RegexValidator(regex=r"^(\+\d{1,3})?,?\s?\d{8,13}")
    Phone = models.CharField('Phone Customer', validators=[PhoneNumberRegex], max_length=16, unique=True)
    Address = models.CharField('Address Customer', max_length=100)
    Birthdate = models.DateField('Birthdate Customer')

    def __str__(self):
        return self.Name


class Car(models.Model):
    Owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Manufacturer = models.CharField('Manufacturer', max_length=50)
    Model = models.CharField('Model', max_length=100)
    YearOfManufacture = models.IntegerField('Year of manufacture')

    def __str__(self):
        return self.Manufacturer


class Order(models.Model):
    Car = models.ForeignKey(Car, on_delete=models.CASCADE)
    User = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Date = models.DateField('Date', auto_now_add=True)
    Amount = models.DecimalField('Amount($)', max_digits=11, decimal_places=5)
    For_status = (
        ('process', 'process'),
        ('done', 'done'),
    )
    Status = models.CharField(max_length=7, choices=For_status, default='unknown')
