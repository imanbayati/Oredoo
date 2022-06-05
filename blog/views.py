from django.shortcuts import render , get_object_or_404
from blog.models import Post,Category,Comment
from taggit.models import Tag
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from blog.forms import CommentForm
from django.contrib import messages
# Create your views here.
def blog_home_page(request,**kwargs):
    posts = Post.objects.filter(status=1)
    recent_posts = Post.objects.filter(status=1)
    recent_posts = recent_posts[:4]
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('tag_name'):
        posts = posts.filter(tag__name__in=[kwargs['tag_name']])
    posts = Paginator(posts,4)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1) 
    tags = Tag.objects.all()
    categories = Category.objects.all()
    context = {'posts':posts,'categories':categories,'tags':tags,'recent_posts':recent_posts}
    return render(request, 'blog/home.html',context)
    

def blog_single_page(request,pid):
    post = get_object_or_404(Post,pk=pid)
    recent_posts = Post.objects.filter(status=1)
    recent_posts = recent_posts[:4]
    tags = Tag.objects.all()
    comments = Comment.objects.filter(post=post.id,approved=True)
    categories = Category.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'your comment submited')
        else:
            messages.error(request,'your comment not submited')
    form = CommentForm()
    context = {'post':post,'categories':categories,'tags':tags,'form':form,'comments':comments,'recent_posts':recent_posts}
    return render(request,'blog/single.html',context)

def blog_search_page(request):
    tags = Tag.objects.all()
    categories = Category.objects.all()
    recent_posts = Post.objects.filter(status=1)
    recent_posts = recent_posts[:4]
    if request.method == 'GET':
        result = request.GET.get('s')
        posts = Post.objects.filter(content__contains=result)
        if posts:
            context = {'categories':categories,'tags':tags,'recent_posts':recent_posts,'posts':posts}
            return render(request,'blog/home.html',context)
        else:
            return render(request,'404.html')
