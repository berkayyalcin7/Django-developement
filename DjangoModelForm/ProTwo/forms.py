# -*- coding: utf-8 -*-
from django.forms import forms,ModelForm
from ProTwo.models import User


#Model ile Formu entegre etmek Django 1.10'da -> ModelForm olarak Django 2.xx -> forms.ModelForm
class NewUserForm(ModelForm):

    class Meta:
        model=User
        fields = '__all__'




