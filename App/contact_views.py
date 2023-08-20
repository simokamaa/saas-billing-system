from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from . forms import *

#view for creating a single contact
def contact_create(request):
    if request.method == 'POST':
        form = contactsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = contactsForm()
    form = contactsForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, "Dashboard/contact_create.html", context)

#view for updating a single contact

def contact_detail(request, pk):
    if request.method == 'POST':
        form = contactsForm(request.POST, instance=contacts)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = contactsForm(request.POST, instance=contacts)
        context = {
            'form' : form
        }
    return render(request, "Dashboard/contact_update.html", context)

#view for viewing a single contact detail

def contact_update(request, pk):
    contacts = get_object_or_404(contacts, pk=pk)
    context = {
        'contacts' : contacts
    }
    return render(request, "Dashboard/contact_detail.html", context)

#view for deleting single contact

def contact_delete(request, pk):
    if request.method == 'POST':
        contact_delete = get_object_or_404(contacts, pk=pk).delete()
        return redirect('/')

#view for deleting all contacts
def contacts_delete(request):
    return contacts.objects.all.delete()
    
#view for contact details

def contacts_detail(request):
    company_contacts = contacts.objects.all()
    context = {
        " company_contacts" : company_contacts
    }
    return render(request, "Dashboard/contacts_detail.html", context)