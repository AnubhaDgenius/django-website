from django import forms
from gallery.models import Owner
from django.urls.base import reverse_lazy
from captcha.fields import CaptchaField 
class MyForm(forms.ModelForm):
    captcha = CaptchaField()    
    class Meta:
        model = Owner
        fields = ['name','myimg','name_pet','type', 'breed','age_pet', 'myimg_pet']
