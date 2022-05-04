from rest_framework import viewsets, permissions

from .serializers import CustomerSerializer
from . import models

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CustomerSerializer