from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from . forms import *

#view for creating a single order_item
def order_item_create(request):
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = OrderItemForm()
    form = OrderItemForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, "Dashboard/order_item_create.html", context)

#view for updating a single order_item

def order_item_update(request, pk):
    if request.method == 'POST':
        form = OrderItemForm(request.POST, instance=OrderItem)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = OrderItemForm(request.POST, instance=OrderItem)
        context = {
            'form' : form
        }
    return render(request, "index.html", context)

#view for viewing a single order_items detail

def order_item_detail(request, pk):
    company_order_item = get_object_or_404(OrderItem, pk=pk)
    context = {
        'company_order_item' : company_order_item
    }
    return render(request, "index.html", context)

#view for deleting single order_item

def order_item_delete(request, pk):
    if request.method == 'POST':
        order_item_delete = get_object_or_404(OrderItem, pk=pk).delete()
        return redirect('/')

#view for deleting all order_items
def order_items_delete(request):
    return OrderItem.objects.all.delete()
    
#view for order_item details

def order_items_detail(request):
    company_order_items = OrderItem.objects.all()
    context = {
        "order_items" : company_order_items
    }
    return render(request, "index.html", context)