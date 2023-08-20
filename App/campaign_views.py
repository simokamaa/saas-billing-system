from django.shortcuts import get_object_or_404, render,redirect
from . models import *
from . forms import *

#view for creating a single campaign
def campaign_create(request):
    if request.method == 'POST':
        form = campaignForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            form = campaignForm()
    form = campaignForm(request.POST)
    context = {
        'form' : form
    }
    return render(request, "Dashboard/campaign_create.html", context)

#view for updating a single campaign
def campaign_detail(request, pk):
    if request.method == 'POST':
        form = campaignForm(request.POST, instance=campaign)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = campaignForm(request.POST, instance=campaign)
        context = {
            'form' : form
        }
    return render(request, "Dashboard/campaign_update.html", context)

#view for viewing a single client detail

def campaign_update(request, pk):
    campaigns = get_object_or_404(Client, pk=pk)
    context = {
        'campaigns' : campaigns   
        }
    return render(request, "Dashboard/campaign_detail.html", context)

#view for deleting single campaign

def campaign_delete(request, pk):
    if request.method == 'POST':
        campaign_delete = get_object_or_404(campaign, pk=pk).delete()
        return redirect('/')

#view for deleting all campaigns
def campaigns_delete(request):
    return campaign.objects.all.delete()
    
#view for campaign details

def campaigns_detail(request):
    company_campaigns = campaign.objects.all()
    context = {
        " company_campaigns" : company_campaigns
    }
    return render(request, "Dashboard/campaigns_detail.html", context)