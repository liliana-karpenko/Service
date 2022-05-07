from cProfile import Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import CustomerForm, CarForm, OrderForm
from users.forms import UserCreationForm
from .models import Customer, Car, Order , User
from django.urls import reverse
from django.contrib.auth.models import Group


@login_required
def customer_home(request):
    customer = Customer.objects.all()
    if request.user.is_anonymous:
        role = 'anonymous'
    else:
        role = Group.objects.filter(user = request.user)[0].name
    print(role == "admin")

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        print(form.is_valid())
    return render(request, 'customer.html', {'customer': customer,
                                             'form_customer': CustomerForm(),
                                             'role': role})

@login_required
def car_home(request):
    car = Car.objects.all()
    if request.user.is_anonymous:
        role = 'anonymous'
    else:
        role = Group.objects.filter(user = request.user)[0].name
    print(role == "admin")
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'car.html', {'car': car,
                                        'form_car': CarForm(),
                                        'role': role})

@login_required
def order_home(request):
    if request.user.is_anonymous:
        role = 'anonymous'
    else:
        role = Group.objects.filter(user = request.user)[0].name
    print(role == "admin")
    order = Order.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'order.html', {'order': order,
                                          'form_order': OrderForm(),
                                            'role': role})


class Register(View):
    temptate_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.temptate_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            my_group = Group.objects.get(name='Worker')
            my_group.user_set.add(user)
            login(request, user)
            return redirect('customer_home')
        context = {
            'form': form
        }
        return render(request, self.temptate_name, context)

@permission_required('users.can_change')
def edit_customer(request, pk):
    get_customer = Customer.objects.get(pk=pk)
    if request.method == 'POST' and Group.objects.filter(user = request.user)[0].name != 'Worker':
        form = CustomerForm(request.POST, instance=get_customer)
        if form.is_valid():
            form.save()

    return render(request, 'customer.html', {'get_customer': get_customer,
                                             'edit_customer': True,
                                             'form_customer': CustomerForm(instance=get_customer)})


def order_details(request, pk):
    order = Order.objects.get(pk=pk)

    print(order)

    return render(request, 'order.html', {'det_order': order,
                                          'details': True})

@permission_required('users.can_change')
def edit_car(request, pk):
    get_car = Car.objects.get(pk=pk)

    if request.method == 'POST':
        print("caaaaaaaaaaaaaaar")
        form = CarForm(request.POST, instance=get_car)
        if form.is_valid():
            form.save()

    return render(request, 'car.html', {'get_car': get_car,
                                        'edit_car': True,
                                        'form_car': CarForm(instance=get_car)})

@permission_required('users.can_change')
def edit_order(request, pk):
    get_order = Order.objects.get(pk=pk)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=get_order)
        if form.is_valid():
            form.save()

    return render(request, 'order.html', {'get_order': get_order,
                                          'edit_order': True,
                                          'form_order': OrderForm(instance=get_order)})

@permission_required('users.can_delete')
def delete_customer(request, pk):
    get_customer = Customer.objects.get(pk=pk)
    get_customer.delete()
    return redirect(reverse("customer_home"))

@permission_required('users.can_delete')
def delete_car(request, pk):
    get_car = Car.objects.get(pk=pk)
    get_car.delete()
    return redirect(reverse("car_home"))

@permission_required('users.can_delete')
def delete_order(request, pk):
    get_order = Order.objects.get(pk=pk)
    get_order.delete()
    return redirect(reverse("order_home"))
