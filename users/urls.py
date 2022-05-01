from django.urls import path, include
from users.views import Register

from django.views.generic import TemplateView
from . import views
from .views import customer_home, car_home, order_home, order_details, edit_customer, edit_order, edit_car, \
    delete_customer, delete_car, delete_order

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('', customer_home, name='customer_home'),
    path('car/', car_home, name='car_home'),
    path('order/', order_home, name='order_home'),
    path('order_details/<int:pk>', order_details, name='order_details'),
    path('edit_customer/<int:pk>', edit_customer, name='edit_customer'),
    path('edit_cur/<int:pk>', edit_car, name='edit_car'),
    path('edit_order/<int:pk>', edit_order, name='edit_order'),
    path('delete_customer/<int:pk>', delete_customer, name='delete_customer'),
    path('delete_car/<int:pk>', delete_car, name='delete_car'),
    path('delete_order/<int:pk>', delete_order, name='delete_order'),

]
