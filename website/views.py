from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post,Category
from website.forms import NewsletterForm,ContactForm
from django.contrib import messages


# Create your views here.

def home_page(request):
    categoies = Category.objects.all()
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'email submited')
        else:
            messages.error(request,'email was not submited')
    form = NewsletterForm() 
    context = {'categoies': categoies,"form":form}
    return render(request,'website/home.html',context)

def about_page(request):
    return render(request,'website/about.html')

def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'your message was sent')
        else:
            messages.error(request,'your message was not sent')
    form = ContactForm()
    context = {'form':form}
    return render(request,'website/contact.html',context)
