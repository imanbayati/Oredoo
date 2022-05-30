from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post,Category


# Create your views here.

def home_page(request):
    categoies = Category.objects.all()
    context = {'categoies': categoies}
    return render(request,'website/home.html',context)

def about_page(request):
    return render(request,'website/about.html')

def contact_page(request):
    return render(request,'website/contact.html')