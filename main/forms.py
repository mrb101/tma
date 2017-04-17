from django import forms
from django.forms import ModelForm
from django.forms.widgets import TextInput, Select, EmailInput, NumberInput, Textarea

from .models import Merchant, Inquiry


class InquiryForm(ModelForm):
    class Meta:
        model = Inquiry
        fields = [
            'name',
            'phone',
            'email',
            'message',
        ]
        widgets = {
            'name': TextInput(
                attrs= {
                    'class': 'form-control',
                    'placeholder': 'Name',
                }
            ),
            'phone': TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Phone',
                }
            ),
            'email': EmailInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Email',
                }
            ),
            'message': Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Message',
                }
            )
        }



class MerchantForm(ModelForm):
    class Meta:
        model = Merchant
        fields = [
            'company',
            'salutation',
            'f_name',
            'l_name',
            'email',
            'mobile',
            'website',
            'street',
            'state',
            'city',
            'zip_code',
            'industry',
            'salay',
            'description',
            'bank',
            'lead_source',
            'contact_method',
        ]
        widgets = {
            'company': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Company',
                }
            ),
            'salutation': Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Salutation',
                }
            ),
            'f_name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'First Name',
                }
            ),
            'l_name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Last Name',
                }
            ),
            'email': EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email',
                }
            ),
            'mobile': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Mobile',
                }
            ),
            'website': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Website',
                }
            ),
            'street': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Street',
                }
            ),
            'state': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'State',
                }
            ),
            'zip_code': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Zip Code',
                }
            ),

            'city': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'City',
                }
            ),
            'industry': Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Industry',
                }
            ),
            'salay': NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Monthly Sales (MYR)',
                }
            ),
            'description': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Description',
                    'rows': 3,
                }
            ),
            'bank': Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Bank',
                }
            ),
            'lead_source': Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Lead Source',
                }
            ),
            'contact_method': Select(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Prefered Method of Contact',
                }
            ),
        }
