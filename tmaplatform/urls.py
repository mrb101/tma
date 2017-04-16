"""tmaplatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from main import views as main_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', main_views.home, name='home'),
    url(r'^about/', main_views.about, name='about'),
    url(r'^services/', main_views.services, name='services'),
    url(r'^contact/', main_views.contact, name='contact'),
    url(r'^signup/', main_views.signup, name='signup'),
    url(r'^m_signup/', main_views.m_signup, name='m_signup'),
    url(r'^inquiry/', main_views.inquiry, name='inquiry'),
    url(r'^$', main_views.home, name='home'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ADMIN HEADER
admin.site.site_header = 'The Merchant Affilate'
