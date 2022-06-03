from django.shortcuts import render , get_object_or_404
from blog.models import Post,Category
from taggit.models import Tag

# Create your views here.
def blog_home_page(request,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('tag_name'):
        posts = posts.filter(tag__name__in=[kwargs['tag_name']])
    tags = Tag.objects.all()
    categories = Category.objects.all()
    context = {'posts':posts,'categories':categories,'tags':tags}
    return render(request, 'blog/home.html',context)
    

def blog_single_page(request,pid):
    post = get_object_or_404(Post,pk=pid)
    tags = Tag.objects.all()
    categories = Category.objects.all()
    context = {'post':post,'categories':categories,'tags':tags}
    return render(request,'blog/single.html',context)

def blog_search_page(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        result = request.GET.get('s')
        posts = posts.filter(content__contains=result)
        if posts:
            context = {'posts':posts}
            return render(request,'blog/home.html',context)
        else:
            return render(request,'404.html')
