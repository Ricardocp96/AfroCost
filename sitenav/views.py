from django.http import HttpResponse
from django.shortcuts import render, redirect
def homepage(request):
   return render(request, 'home.html')


def navigator(request):
    return render(request, 'Contact.html')