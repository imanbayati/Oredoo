from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home_page(request):
    return render(request,'website/home.html')

def about_page(request):
    return render(request,'website/about.html')

def contact_page(request):
    return render(request,'website/contact.html')