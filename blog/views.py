from django.shortcuts import render , get_object_or_404
from blog.models import Post,Category
# Create your views here.
def blog_home_page(request,cat_name=None):
    posts = Post.objects.filter(status=1)
    if cat_name != None:
        posts = posts.filter(category__name=cat_name)
    categories = Category.objects.all()
    context = {'posts':posts,'categories':categories}
    return render(request, 'blog/home.html',context)
    

def blog_single_page(request,pid):
    post = get_object_or_404(Post,pk=pid)
    categories = Category.objects.all()
    context = {'post':post,'categories':categories}
    return render(request,'blog/single.html',context)

def blog_category_page(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request,'blog/home.html',context)
