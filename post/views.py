from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib import messages 
from accounts.models import UserAccount
from django.db.models import Q
# Create your views here.

def check_login(request):
    user_id=request.session.get('user_id')
    if user_id:
        return UserAccount.objects.get(id=user_id)
    else:
        return False


def index(request):
    return redirect('post_list')

def post_list(request, category=None,id=None):
    user=False
    
    if check_login(request):
        user=check_login(request)
   

    CATEGORY_DICT = dict(Post.CATEGORY_CHOICES)
    category_name=CATEGORY_DICT.get(category)
    if category:
        posts = Post.objects.filter(category=category)
        
    else:
        posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts, 'category': category_name,'user':user,'query':None})

def search_post(request):
    user=False
    
    if check_login(request):
        user=check_login(request)
    query=request.GET.get('query')

    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    else:
        return redirect('post_list')
    return render(request,'post_list.html',{'posts':posts,'user':user,'query':query,'category': None})


def post_create(request):
    user=None
    
    if check_login(request):
        user=check_login(request)
    else:
        messages.error(request,"請先登入")
        return redirect('login')
    if request.method == 'POST':
       
        form = PostForm(request.POST)
        form.user=user
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form,'user':user})

def article_post(request,id):
    user=None
    if check_login(request):
        user=check_login(request)

    if id:
        article=Post.objects.get(id=id)
        same_article=Post.objects.filter(category=article.category).exclude(id=id)
        if article:
            return render(request,'article.html',{'article':article,'same_article':same_article,'user':user,'category':article.get_category_display})
        else:
            return redirect('post_list')
    else:
        return redirect('post_list')
    