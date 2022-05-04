from rest_framework import viewsets, permissions

from .serializers import CustomerSerializer, CarSerializer, OrderSerializer
from . import models

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CustomerSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = models.Car.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CarSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = OrderSerializer