from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from . forms import *

#view for creating a single client
def client_create(request):
    if request.method == 'POST':
        form = clientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = clientForm()
    form = clientForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, "Dashboard/client_create.html", context)

#view for updating a single client

def client_update(request, pk):
    if request.method == 'POST':
        form = clientForm(request.POST, instance=Client)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = clientForm(request.POST, instance=Client)
        context = {
            'form' : form
        }
    return render(request, "Dashboard/client_update.html", context)

#view for viewing a single client detail

def client_detail(request, pk):
    company_client = get_object_or_404(Client, pk=pk)
    context = {
        'company_client' : company_client
    }
    return render(request, "Dashboard/client_detail.html", context)

#view for deleting single client

def client_delete(request, pk):
    client_delete = get_object_or_404(Client, pk=pk)
    client_delete.delete()
    return redirect('/')

#view for deleting all clients
def clients_delete(request):
    clients = Client.objects.all()
    clients.delete()
    return redirect('/')

    
#view for client details

def clients_detail(request):
    company_clients = Client.objects.all()
    context = {
        "company_clients" : company_clients
    }
    return render(request, "Dashboard/clients_detail.html", context)