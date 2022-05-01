from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Customer, Car, Order

admin.site.register(Customer)
admin.site.register(Car)
admin.site.register(Order)

User = get_user_model()


@admin.register(User)
class UserAdmin(UserAdmin):
    pass
