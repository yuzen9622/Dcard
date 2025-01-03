from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post,Comment
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
        comment=Comment.objects.filter(post=article)
        if article:
            return render(request,'article.html',{'article':article,'same_article':same_article,'user':user,'category':article.get_category_display,'comments':comment})
        else:
            return redirect('post_list')
    else:
        return redirect('post_list')
    
def comment_post(request):
    user=None
    if check_login(request):
        user=check_login(request)
    if request.method == 'POST':
        content=request.POST.get('content')
        post_id=request.POST.get('post_id')
        if content and user and post_id:
            post=Post.objects.get(id=post_id)
            comment=Comment(poster=user,content=content,post=post)
            comment.save()
            return redirect('article_post',id=post_id)
    return redirect('post_list')
def comment_delete(request,id):
    user=None
    if check_login(request):
        user=check_login(request)
    if id:
        comment=Comment.objects.get(id=id)
        if comment.poster==user:
            post_id=comment.post.id
            comment.delete()
            return redirect('article_post',id=post_id)
    return redirect('post_list')

def comment_edit(request,id):
    user=None
    if check_login(request):
        user=check_login(request)
    if id:
        comment=Comment.objects.get(id=id)
        if comment.poster==user:
            if request.method == 'POST':
                content=request.POST.get('content')
                comment.content=content
                comment.save()
                return redirect('article_post',id=comment.post.id)
        else:
            return redirect('post_list')
        return render(request,'comment_edit.html',{'comment':comment})
    return redirect('post_list')
