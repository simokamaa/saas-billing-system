from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from . forms import *
from datetime import datetime
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, "Dashboard/index.html")

# payment views
def payments(request):
    return render(request, "Dashboard/payments.html")

# daily report views
def dailyReports(request):
    date = datetime.now()
    context = {
        'date' : date
    }
    return render(request, "Dashboard/dailyReports.html", context)

#  Monthly Report views
def monthlyReports(request):
    date = datetime.now()
    context = {
        'date' : date
    }
    return render(request, "Dashboard/monthlyReports.html", context)

# Yearly Reports views
def yearlyReports(request):
    date = datetime.now()
    context = {
        'date' : date
    }
    return render(request, "Dashboard/yearlyReports.html", context)

# settings module
def settings(request):
    return render(request, "Dashboard/settings.html")

# profile
def profile(request):
    return render(request, "Dashboard/profile.html")


# login function
def login(request):
    pass

# logout function
def logout(request):
    pass