from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from . forms import *

#view for creating a single package
def package_create(request):
    if request.method == 'POST':
        form = PackagesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = PackagesForm()
    form = PackagesForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, "Dashboard/package_create.html", context)

#view for updating a single package

def package_update(request, pk):
    if request.method == 'POST':
        form = PackagesForm(request.POST, instance=Packages)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = PackagesForm(request.POST, instance=Packages)
        context = {
            'form' : form
        }
    return render(request, "Dashboard/package_update.html", context)

#view for viewing a single Packages detail

def package_detail(request, pk):
    company_package = get_object_or_404(Packages, pk=pk)
    context = {
        'company_package' : company_package
    }
    return render(request, "Dashboard/package_detail.html", context)

#view for deleting single package

def package_delete(request, pk):
    if request.method == 'POST':
        package_delete = get_object_or_404(Packages, pk=pk).delete()
        return redirect('/')

#view for deleting all packages
def packages_delete(request):
    return Packages.objects.all.delete()
    
#view for package details

def packages_detail(request):
    company_packages = Packages.objects.all()
    context = {
        "packages" : company_packages
    }
    return render(request, "Dashboard/packages_detail.html", context)