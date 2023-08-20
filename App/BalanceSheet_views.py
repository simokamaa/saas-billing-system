from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from . forms import *


def BalanceSheet(request):
    return render(request, "Dashboard/balanceSheet.html")