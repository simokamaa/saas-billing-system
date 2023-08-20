from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from . forms import *

#view for creating a single email_module
def email_module_create(request):
    if request.method == 'POST':
        form = email_moduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = email_moduleForm()
    form = email_moduleForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, "Dashboard/email_module_create.html", context)

#view for updating a single email_module

def email_module_update(request, pk):
    if request.method == 'POST':
        form = email_moduleForm(request.POST, instance=email_module)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = email_moduleForm(request.POST, instance=email_module)
        context = {
            'form' : form
        }
    return render(request, "Dashboard/email_module_update.html", context)

#view for viewing a single email_modules detail

def email_module_detail(request, pk):
    company_email_module = get_object_or_404(email_module, pk=pk)
    context = {
        'company_email_module' : company_email_module
    }
    return render(request, "Dashboard/email_module_detail.html", context)

#view for deleting single email_module

def email_module_delete(request, pk):
    if request.method == 'POST':
        email_module_delete = get_object_or_404(email_module, pk=pk).delete()
        return redirect('/')

#view for deleting all email_modules
def email_modules_delete(request):
    return email_module.objects.all.delete()
    
#view for email_module details

def email_modules_detail(request):
    company_email_modules = email_module.objects.all()
    context = {
        "email_modules" : company_email_modules
    }
    return render(request, "Dashboard/email_modules_detail.html", context)