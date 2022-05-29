from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('',blog_home_page,name='home'),
    path('post/<int:pid>',blog_single_page,name='single')
]
