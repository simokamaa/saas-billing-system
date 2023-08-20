from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from . forms import *

#view for creating a single order
def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = OrderForm()
    form = OrderForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, "Dashboard/order_create.html", context)

#view for updating a single order

def order_update(request, pk):
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=Order)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = OrderForm(request.POST, instance=Order)
        context = {
            'form' : form
        }
    return render(request, "order_update.html", context)

#view for viewing a single orders detail

def order_detail(request, pk):
    company_order = get_object_or_404(Order, pk=pk)
    context = {
        'company_order' : company_order
    }
    return render(request, "index.html", context)

#view for deleting single order

def order_delete(request, pk):
    if request.method == 'POST':
        order_delete = get_object_or_404(Order, pk=pk).delete()
        return redirect('/')

#view for deleting all orders
def orders_delete(request):
    return Order.objects.all.delete()
    
#view for order details

def orders_detail(request):
    company_orders = Order.objects.all()
    context = {
        "orders" : company_orders
    }
    return render(request, "Dashboard/orders_detail.html", context)