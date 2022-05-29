from django.shortcuts import render , get_object_or_404
from blog.models import Post,Category
# Create your views here.
def blog_home_page(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request, 'blog/home.html',context)

def blog_single_page(request,pid):
    post = get_object_or_404(Post,pk=pid)
    context = {'post': post}
    return render(request,'blog/single.html',context)
