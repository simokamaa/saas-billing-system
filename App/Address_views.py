from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from . forms import *

#view for creating a single Address
def Address_create(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = AddressForm()
    form = AddressForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, "Dashboard/Address_create.html", context)

#view for updating a single Address

def Address_update(request, pk):
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=Address)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = AddressForm(request.POST, instance=Address)
        context = {
            'form' : form
        }
    return render(request, "index.html", context)

#view for viewing a single Address detail

def Address_detail(request, pk):
    company_Address = get_object_or_404(Address, pk=pk)
    context = {
        'company_Address' : company_Address
    }
    return render(request, "index.html", context)

#view for deleting single Address

def Address_delete(request, pk):
    if request.method == 'POST':
        Address_delete = get_object_or_404(Address, pk=pk).delete()
        return redirect('/')

#view for deleting all Addresss
def Addresss_delete(request):
    return Address.objects.all.delete()
    
#view for Address details

def Address_details(request):
    company_Address = Address.objects.all()
    context = {
        "Address" : company_Address
    }
    return render(request, "index.html", context)