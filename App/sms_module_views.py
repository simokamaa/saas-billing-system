from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from . forms import *

#view for creating a single sms_module
def sms_module_create(request):
    if request.method == 'POST':
        form = sms_moduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = sms_moduleForm()
    form = sms_moduleForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, "Dashboard/sms_module_create.html", context)

#view for updating a single sms_module

def sms_module_update(request, pk):
    if request.method == 'POST':
        form = sms_moduleForm(request.POST, instance=sms_module)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = sms_moduleForm(request.POST, instance=sms_module)
        context = {
            'form' : form
        }
    return render(request, "Dashboard/sms_module_update.html", context)

#view for viewing a single sms_modules detail

def sms_module_detail(request, pk):
    company_sms_module = get_object_or_404(sms_module, pk=pk)
    context = {
        'company_sms_module' : company_sms_module
    }
    return render(request, "Dashboard/sms_module_detail.html", context)

#view for deleting single sms_module

def sms_module_delete(request, pk):
    if request.method == 'POST':
        sms_module_delete = get_object_or_404(sms_module, pk=pk).delete()
        return redirect('/')

#view for deleting all sms_modules
def sms_modules_delete(request):
    return sms_module.objects.all.delete()
    
#view for sms_module details

def sms_modules_detail(request):
    company_sms_modules = sms_module.objects.all()
    context = {
        "company_sms_modules" : company_sms_modules
    }
    return render(request, "Dashboard/sms_modules_detail.html", context)