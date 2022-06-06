from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('login',login_page,name='login'),
    path('signup',sign_up_page,name='signup'),
    path('logout',logout_page,name='logout'),
]
