from django.shortcuts import render , get_object_or_404
from blog.models import Post,Category
# Create your views here.
def blog_home_page(request):
    posts = Post.objects.filter(status=1)
    #posts = get_object_or_404(posts)
    context = {'posts':posts}
    return render(request, 'blog/home.html',context)

def blog_single_page(request):
    return render(request,'blog/single.html')