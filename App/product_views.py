from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from . forms import *

#view for creating a single product
def product_create(request):
    if request.method == 'POST':
        form = ProductItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = ProductItemForm()
    form = ProductItemForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, "Dashboard/product_create.html", context)

#view for updating a single product

def product_update(request, pk):
    if request.method == 'POST':
        form = ProductItemForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = ProductItemForm(request.POST, instance=product)
        context = {
            'form' : form
        }
    return render(request, "Dashboard/product_update.html", context)

#view for viewing a single product detail

def product_detail(request, pk):
    company_product = get_object_or_404(ProductItem, pk=pk)
    context = {
        'company_product' : company_product
    }
    return render(request, "Dashboard/product_detail.html", context)

#view for deleting single product

def product_delete(request, pk):
    if request.method == 'POST':
        product_delete = get_object_or_404(ProductItem, pk=pk).delete()
        return redirect('/')

#view for deleting all products
def products_delete(request):
    return ProductItem.objects.all.delete()
    
#view for product details

def products_detail(request):
    company_products = ProductItem.objects.all()
    context = {
        "products" : company_products
    }
    return render(request, "Dashboard/products_detail.html", context)