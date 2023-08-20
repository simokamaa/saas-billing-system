from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from . forms import *

#view for creating a single Refund
def Refund_create(request):
    if request.method == 'POST':
        form = RefundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = RefundForm()
    form = RefundForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, "Dashboard/Refund_create.html", context)

#view for updating a single Refund

def Refund_update(request, pk):
    if request.method == 'POST':
        form = RefundForm(request.POST, instance=Refund)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = RefundForm(request.POST, instance=Refund)
        context = {
            'form' : form
        }
    return render(request, "Dashboard/Refund_update.html", context)

#view for viewing a single Refund detail

def Refund_detail(request, pk):
    company_Refund = get_object_or_404(Refund, pk=pk)
    context = {
        'company_Refund' : company_Refund
    }
    return render(request, "Dashboard/Refund_detail.html", context)

#view for deleting single Refund

def Refund_delete(request, pk):
    if request.method == 'POST':
        Refund_delete = get_object_or_404(Refund, pk=pk).delete()
        return redirect('/')

#view for deleting all Refunds
def Refunds_delete(request):
    return Refund.objects.all.delete()
    
#view for Refund details

def Refunds_detail(request):
    company_Refunds = Refund.objects.all()
    context = {
        "company_Refunds" : company_Refunds
    }
    return render(request, "Dashboard/Refunds_detail.html", context)