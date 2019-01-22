# -*- coding: utf-8 -*-
from django.shortcuts import render
from ProTwo.models import User
# Formu import ettik.
from ProTwo.forms import NewUserForm

def index(request):
    return render(request,'ProTwo/index.html')

"""
def users(request):
    user_list=User.objects.order_by('first_name')
    user_dict={'users':user_list}
    return render(request,'ProTwo/users.html',context=user_dict)
"""

def users(request):

    form=NewUserForm()

    if request.method=="POST":
        form=NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error form invalid')

    return render(request,'ProTwo/users.html',{'form':form})

