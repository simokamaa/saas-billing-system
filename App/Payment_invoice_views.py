from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from . forms import *

#view for creating a single payment_invoice
def payment_invoice_create(request):
    if request.method == 'POST':
        form = payement_invoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = payement_invoiceForm()
    form = payement_invoiceForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, "Dashboard/payment_invoice_create.html", context)

#view for updating a single payment_invoice

def payment_invoice_update(request, pk):
    if request.method == 'POST':
        form = payement_invoiceForm(request.POST, instance=payment_invoice)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = payement_invoiceForm(request.POST, instance=payment_invoice)
        context = {
            'form' : form
        }
    return render(request, "payment_invoice_update.html", context)

#view for viewing a single payment_invoice detail

def payment_invoice_detail(request, pk):
    company_payment_invoice = get_object_or_404(payment_invoice, pk=pk)
    context = {
        'company_payment_invoice' : company_payment_invoice
    }
    return render(request, "Dashboard/payment_invoice_detail.html", context)

#view for deleting single payment_invoice

def payment_invoice_delete(request, pk):
    if request.method == 'POST':
        payment_invoice_delete = get_object_or_404(payment_invoice, pk=pk).delete()
        return redirect('/')

#view for deleting all payment_invoices
def payment_invoices_delete(request):
    return payment_invoice.objects.all.delete()
    
#view for payment_invoice details

def payment_invoices_detail(request):
    company_payment_invoices = payment_invoice.objects.all()
    context = {
        "payment_invoices" : company_payment_invoices
    }
    return render(request, "Dashboard/payment_invoices_detail.html", context)