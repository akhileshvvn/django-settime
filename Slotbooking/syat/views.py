from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import formf
# Create your views here.


def error(request,mess):
    msg = { 'msgs' : mess}
    return render(request,template_name='syat/error.html',context=msg)


def fill(request):
    form = formf()
    if User.is_authenticated:
        if request.method == 'POST':
            form = formf(request.POST)
            if form.is_valid():
                form.save()
                print('success')
                return render(request,'syat/error.html',{'msgs':"YOUR AVAILABLE TIME HAS BEEN SET"})
        else:
            form = formf()
    return render(request,'syat/fillform.html',{'form':form})


def book(request):
    return render(request,'syat/book.html')