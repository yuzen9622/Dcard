from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
# Create your views here.

def index(request):
    return HttpResponse("hello world")

def post_list(request, category=None):
    CATEGORY_DICT = dict(Post.CATEGORY_CHOICES)
    category_name=CATEGORY_DICT.get(category)
    if category:
        posts = Post.objects.filter(category=category)
        
    else:
        posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts, 'category': category_name})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})

def article_post(request,id):
    if id:
        article=Post.objects.get(id=id)
        if article:
            return render(request,'article.html',{'article':article})
        else:
            return redirect('post_list')
    else:
        return redirect('post_list')
    