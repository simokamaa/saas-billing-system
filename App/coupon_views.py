from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from . forms import *

#view for creating a single coupon
def coupon_create(request):
    if request.method == 'POST':
        form = CouponForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = CouponForm()
    form = CouponForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, "Dashboard/coupon_create.html", context)

#view for updating a single coupon

def coupon_update(request, pk):
    if request.method == 'POST':
        form = CouponForm(request.POST, instance=Coupon)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = CouponForm(request.POST, instance=Coupon)
        context = {
            'form' : form
        }
    return render(request, "index.html", context)

#view for viewing a single coupon detail

def coupon_detail(request, pk):
    company_coupon = get_object_or_404(Coupon, pk=pk)
    context = {
        'company_coupon' : company_coupon
    }
    return render(request, "index.html", context)

#view for deleting single coupon

def coupon_delete(request, pk):
    if request.method == 'POST':
        coupon_delete = get_object_or_404(Coupon, pk=pk).delete()
        return redirect('/')

#view for deleting all coupons
def coupons_delete(request):
    return Coupon.objects.all.delete()
    
#view for coupon details

def coupons_detail(request):
    company_coupons = Coupon.objects.all()
    context = {
        "coupons" : company_coupons
    }
    return render(request, "index.html", context)