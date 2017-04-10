# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

import json
import urllib
import urllib2
import requests

from .models import (
    MainBody,
    Clients,
    Testimony,
    About,
    Team,
    Merchant,
)

from .forms import MerchantForm

from tmaplatform.settings import API, API_KEY, API_SEC


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
        params = {
            'api_key': str(API_KEY),
            'api_secret': str(API_SEC),
            'from': '00601137480800',
            'to': request.POST.get('mobile'),
            'text': "Your Information has been submitted. Thank you! - TMA"
        }
        params2 = {
            'api_key': str(API_KEY),
            'api_secret': str(API_SEC),
            'from': '00601137480800',
            'to': '0060163225617',
            'text': 'New Merchant has registed!',
        }
        url = 'https://rest.nexmo.com/sms/json?' + urllib.urlencode(params)
        url2 = 'https://rest.nexmo.com/sms/json?' + urllib.urlencode(params2)
        req = urllib2.Request(url)
        req2 = urllib2.Request(url2)
        req.add_header('Accept', 'application/json')
        req2.add_header('Accept', 'application/json')
        res = urllib2.urlopen(req)
        res2 = urllib2.urlopen(req2)
        if res.code == 200:
            data = res.read()
            decoded_res = json.loads(data.decode('utf-8'))
            messages = decoded_res["messages"]
            for message in messages:
                if message["status"] == "0":
                    print("Success")
                else:
                    print("Error{0}".format(res.code))
        if res2.code == 200:
            data = res2.read()
            decoded_res2 = json.loads(data.decode('utf-8'))
            messages2 = decoded_res2["messages"]
            for message2 in messages2:
                if message2["status"] == "0":
                    print("Success")
                else:
                    print("Error{0}".format(res.code))
        send_email_notification(request.POST.get('email'))
        return HttpResponse(json.dumps({
            'type': 'S01',
            'msg': 'Success!'
        }))
    else:
        return HttpResponse(json.dumps({
            'type': 'S02',
            'msg': 'Error!'
        }))

def send_email_notification(email):
    URL = "https://api.mailgun.net/v3/sandboxedba71b9ee904dc5aab7a79a7492098b.mailgun.org/messages"
    params = {
        "from": "TMA <postmaster@sandboxedba71b9ee904dc5aab7a79a7492098b.mailgun.org>",
        "to": [str(email),],
        "subject": "TMA Confirmation",
        "text": "This is an email to confirm your registration to TMA"
    }
    return requests.post(
        URL,
        auth=("api", str(API)),
        data=params
    )
