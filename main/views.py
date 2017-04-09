# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from .models import (
    MainBody,
    Clients,
    Testimony,
    About,
    Team,
    Merchant,
)

from .forms import MerchantForm

def home(request):
    template = 'main/home.html'
    body = ''
    clients = ''
    testimonies = ''
    if MainBody.objects.all().exists():
        body = MainBody.objects.latest('updated')
    if Clients.objects.all().exists():
        clients = Clients.objects.all()
    if Testimony.objects.all().exists():
        testimonies = Testimony.objects.all()
        count = Testimony.objects.count()
    context = {
        'body': body,
        'clients': clients,
        'testimonies': testimonies,
    }
    return render(request, template, context)


def about(request):
    template = 'main/about.html'
    about = ''
    teams = ''
    if About.objects.all().exists():
        about = About.objects.latest('updated')
    if Team.objects.all().exists():
        teams = Team.objects.all()
    context = {'about': about, 'teams': teams}
    return render(request, template, context)


def contact(request):
    template = 'main/contact.html'
    context = {}
    return render(request, template, context)


def services(request):
    template = 'main/services.html'
    context = {}
    return render(request, template, context)


def signup(request):
    template = 'main/signup.html'
    form = MerchantForm
    context = {'form': form}
    return render(request, template, context)


def m_signup(request):
    if request.method == 'POST':
        merchant = Merchant()
        merchant.company = request.POST.get('company')
        merchant.salutation = request.POST.get('salutation')
        merchant.f_name = request.POST.get('f_name')
        merchant.l_name = request.POST.get('l_name')
        merchant.email = request.POST.get('email')
        merchant.mobile = request.POST.get('mobile')
        merchant.website = request.POST.get('website')
        merchant.street = request.POST.get('street')
        merchant.state = request.POST.get('state')
        merchant.zip_code = request.POST.get('zip_code')
        merchant.city = request.POST.get('city')
        merchant.industry = request.POST.get('industry')
        merchant.salay = request.POST.get('salay')
        merchant.description = request.POST.get('description')
        merchant.bank = request.POST.get('bank')
        merchant.lead_source = request.POST.get('lead_source')
        merchant.contact_method = request.POST.get('contact_method')
        merchant.save()
        return HttpResponse(json.dumps({
            'type': 'S01',
            'msg': 'Success!'
        }))
    else:
        return HttpResponse(json.dumps({
            'type': 'S02',
            'msg': 'Error!'
        }))
