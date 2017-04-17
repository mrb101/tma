# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import (
    About,
    Contact,
    Services,
    Clients,
    Base,
    Team,
    Slider,
    MainBody,
    Testimony,
    Merchant,
    Inquiry,
)


admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Services)
admin.site.register(Clients)
admin.site.register(Base)
admin.site.register(Team)
admin.site.register(Slider)
admin.site.register(MainBody)
admin.site.register(Testimony)
admin.site.register(Merchant)
admin.site.register(Inquiry)
