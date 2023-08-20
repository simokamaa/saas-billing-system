from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from . forms import *

#view for creating a single Payment
def Payment_create(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = PaymentForm()
    form = PaymentForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, "Dashboard/Payment_create.html", context)

#view for updating a single Payment

def Payment_update(request, pk):
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=Payment)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = PaymentForm(request.POST, instance=Payment)
        context = {
            'form' : form
        }
    return render(request, "Dashboard/Payment_update.html", context)

#view for viewing a single Payment detail

def Payment_detail(request, pk):
    company_Payment = get_object_or_404(Payment, pk=pk)
    context = {
        'company_Payment' : company_Payment
    }
    return render(request, "Dashboard/Payment_detail.html", context)

#view for deleting single Payment

def Payment_delete(request, pk):
    if request.method == 'POST':
        Payment_delete = get_object_or_404(Payment, pk=pk).delete()
        return redirect('/')

#view for deleting all Payments
def Payments_delete(request):
    return Payment.objects.all.delete()
    
#view for Payment details

def Payments_detail(request):
    company_Payments = Payment.objects.all()
    context = {
        "Payments" : company_Payments
    }
    return render(request, "Dashboard/Payments_detail.html", context)