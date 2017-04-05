# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def home(request):
    template = 'main/home.html'
    context = {}
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
