# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import MainBody, Clients, Testimony


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
    context = {}
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
    context = {}
    return render(request, template, context)
