from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm
from accounts.forms import SignUpForm


# Create your views here.
def login_page(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request = request,data = request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request,username = username, password = password)
                if user is not None:
                    login(request, user)
                    return redirect ('/')
        form = AuthenticationForm()
        context = {'form':form}
        return render(request,'accounts/login.html',context)
    else:
        return redirect('/')

def sign_up_page(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        form = SignUpForm()
        context = {"form":form}
        return render(request,'accounts/sign-up.html',context)
    else:
        return redirect('/')

def logout_page(request):
    logout(request)
    return redirect('/')
