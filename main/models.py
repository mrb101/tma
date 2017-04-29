# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail


class TimeStampModel(models.Model):
    """ Abstract Model for Timestamp """
    created = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        abstract = True


class About(TimeStampModel):
    """ Model that contains the about page information """
    title = models.CharField(max_length=255, null=False, blank=False)
    text = models.TextField()


class Inquiry(TimeStampModel):
    """ Model that contains the about page information """
    name = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    message = models.TextField(null=False, blank=False)


class Contact(TimeStampModel):
    street = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    land_line = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)


class Services(TimeStampModel):
    """ Model that contains the Services page information """
    title = models.CharField(max_length=255, null=False, blank=False)
    Description = models.TextField()
    desc_image = models.ImageField(upload_to='services', null=False, blank=False)


class Clients(TimeStampModel):
    """ Model that contains TMA clients logos and website link """
    link = models.CharField(max_length=255, null=False, blank=False)
    client_logo = models.ImageField(upload_to='clients', null=False, blank=False)
    client_img = ImageSpecField(source='client_logo',
                              processors=[Thumbnail(165, 127.14)],
                              options={'quality': 100})


class Base(TimeStampModel):
    """ Model that contains main template information """
    logo = models.ImageField(upload_to='logo', null=False, blank=False)
    logo_img = ImageSpecField(source='logo',
                              processors=[Thumbnail(400, 40)],
                              options={'quality': 100})
    logo_footer = models.ImageField(upload_to='logo_footer', null=False, blank=False)
    logo_footer_img = ImageSpecField(source='logo_footer',
                                     processors=[Thumbnail(320, 80)],
                                     options={'quality': 100})
    facebook = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    google = models.CharField(max_length=255, null=True, blank=True)
    pintrest = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    copy_text = models.TextField(max_length=1000, null=False, blank=False)
    footer_phone = models.CharField(max_length=50, null=False, blank=False)
    footer_phone_timing = models.CharField(max_length=50, null=False, blank=False)
    footer_address = models.CharField(max_length=255, null=False, blank=False)
    footer_text = models.TextField(null=False, blank=False)


class Team(TimeStampModel):
    """ Model that contains the team information for about page """
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    facebook = models.CharField(max_length=255, null=False, blank=False)
    twitter = models.CharField(max_length=255, null=False, blank=False)
    linkedin = models.CharField(max_length=255, null=False, blank=False)
    team_profile = models.ImageField(upload_to='team_profile', null=False, blank=False)


class Slider(TimeStampModel):
    """ Model that contains the home page slider images and text """
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    slider_image = models.ImageField(upload_to='slider', null=False, blank=False)


class MainBody(TimeStampModel):
    """ Model that contains the home page body image and text """
    title = models.CharField(max_length=255, null=False, blank=False)
    text = models.TextField(null=True, blank=True)
    main_body_image = models.ImageField(upload_to='main_body_image', null=False, blank=False)
    main_body_img = ImageSpecField(source='main_body_image',
                                   processors=[Thumbnail(100, 100)],
                                   options={'quality': 100})


class Testimony(TimeStampModel):
    """ Model that contains the home page testimonies for marketing and reference """
    name = models.CharField(max_length=255, null=False, blank=False)
    title = models.CharField(max_length=255, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    testimony_profile_image = models.ImageField(upload_to='testimony_profile_image', null=False, blank=False)
    testimony_img = ImageSpecField(source='testimony_profile_image',
                              processors=[Thumbnail(80, 80)],
                              options={'quality': 100})
    first = models.BooleanField(default=False)


class Merchant(TimeStampModel):
    """ Model that contain the information for merchants who wants to signup"""
    NONE = 'NONE'
    MR = 'MR'
    MRS = 'MRS'
    MS = 'MS'
    DR = 'DR'
    PROF = 'PROF'
    GN = 'GENERAL RETAIL GOODS/SERVICES'
    FT = 'FITNESS CENTER/GYM'
    BHS = 'BEAUTY, HAIR AND SLIMING'
    MOTO = 'MOTO AND ECOMMERCE'
    EDU = 'EDUCATION'
    DS = 'MLM/DIRECT SELLING'
    AT = 'ALOCHOL/TOBACCO'
    FOX = 'TRADING/FOREX'
    REST = 'RESTURANT/CAFE'
    TOP = 'BILL PAYMENT/MOBILE TOPUP'
    HAND = 'HANDPHONE SHOP/REPAIR'
    RET = 'RETAIL (SHOPPING MALL TENANT)'
    HEAL = 'CLINIC/HEALTHCARE'
    TRANS = 'TRANSPORTATION/CAR RENTAL'
    BAR = 'BAR/NIGHTCLUB'
    ALL = 'ALLIANCE BANK'
    AM = 'AMBANK'
    BIS = 'BANK ISLAM'
    BMU = 'BANK MUAMALAT'
    BSN = 'BSN'
    CIMB = 'CIMB'
    CIT = 'CITIBANK'
    GP = 'GLOBAL PAYMENTS'
    HL = 'HONG LEONG'
    MYB = 'MAYBANK'
    OC = 'OCBC'
    PUB = 'PUBLIC BANK'
    RHB = 'RHB'
    STD = 'STANDARD CHARTERED'
    SYN = 'SYNERGY'
    UOB = 'UOB'
    PHONE = 'PHONE'
    SEARCH = 'SEARCH ENGINE'
    WORD = 'WORD OF MOUTH'
    EMPREF = 'EMPLOYEE REFERRAL'
    OTH = 'OTHER'
    PH = 'PHONE'
    EM = 'EMAIL'
    WA = 'WHATSAPP'
    APP = 'APPOITMENT'
    company = models.CharField(max_length=255, null=False, blank=False)
    SALUTATION = (
        (NONE, 'None'),
        (MR, 'Mr'),
        (MRS, 'Mrs'),
        (MS, 'Ms'),
        (DR, 'Dr'),
        (PROF, 'Prof')
    )
    salutation = models.CharField(choices=SALUTATION, max_length=4, null=False, blank=False)
    f_name = models.CharField(max_length=255, null=False, blank=False)
    l_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False, unique=True)
    mobile = models.CharField(max_length=100, null=False, blank=False, unique=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    INDUSTRY = (
        (NONE, 'None'),
        (GN, 'General Retail Goods/Services'),
        (FT, 'Fitness Centre/Gym'),
        (BHS, 'Beauty, Hair and Slimming'),
        (MOTO, 'MOTO and eCommerce'),
        (EDU, 'Education'),
        (DS, 'MLM/Direct Selling'),
        (AT, 'Alcohol/Tobacco'),
        (FOX, 'Trading/Forex'),
        (REST, 'Restaurant/Cafe'),
        (TOP, 'Bill Payment/Mobile Topup'),
        (HAND, 'Handphone Shop/Repair'),
        (RET, 'Retail (Shopping Mall Tenant)'),
        (HEAL, 'Clinic/Healthcare'),
        (TRANS, 'Transportation/Car Rental'),
        (BAR, 'Bar/Nightclub'),
    )
    industry = models.CharField(choices=INDUSTRY, max_length=255, null=False, blank=False)
    salay = models.IntegerField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    BANK = (
        (ALL, 'Alliance Bank'),
        (AM, 'AmBank'),
        (BIS, 'Bank Islam'),
        (BMU, 'Bank Muamalat'),
        (BSN, 'BSN'),
        (CIMB, 'CIMB'),
        (CIT, 'CitiBank'),
        (GP, 'Global Pyaments'),
        (HL, 'Hong Leong'),
        (MYB, 'MayBank'),
        (OC, 'OCBC'),
        (PUB, 'Public Bank'),
        (RHB, 'RHB'),
        (STD, 'Standard Chartered'),
        (SYN, 'Synergy'),
        (UOB, 'UOB'),
    )
    bank = models.CharField(choices=BANK, max_length=50, null=False, blank=False)
    SOURCE = (
        (PHONE, 'Phone'),
        (SEARCH, 'Search Engine'),
        (WORD, 'Word Of MoUth'),
        (EMPREF, 'Employee Referral'),
        (OTH, 'Other')
    )
    lead_source = models.CharField(choices=SOURCE, max_length=100, null=False, blank=False)
    CONTACT = (
        (PH, 'Phone'),
        (EM, 'Email'),
        (WA, 'WhatsApp'),
        (APP, 'Appointment')
    )
    contact_method = models.CharField(choices=CONTACT, max_length=50, null=False, blank=False)
