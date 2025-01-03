from django.shortcuts import render,redirect
from .models import UserAccount
from django.http import HttpResponseRedirect
from django.contrib import messages  # 引入 messages 系統
from django.contrib.auth import logout
from post.models import Post,Comment
import os
# Create your views here.
def login_user(request):
    user=None
    user_id=request.session.get('user_id')
    if user_id:
        user=UserAccount.objects.get(id=user_id)
        return redirect('post_list')


    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=UserAccount.objects.filter(email=email).first()
        
        if user is None:
            messages.error(request,"電子郵件錯誤")
            return redirect('login')
            
        if user.check_password(password) or user.password==password:
            request.session['user_id']=user.id
            return redirect('post_list')
        else:
            messages.error(request,"密碼錯誤")
            return redirect('login')
    return render(request,"login.html",{'user':user})

def register_user(request):
    user=None
    user_id=request.session.get('user_id')
    if user_id:
        user=UserAccount.objects.get(id=user_id)
        return redirect('post_list')
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        username=request.POST.get('username')
        password_confirm = request.POST.get('password_confirm')
        # 檢查密碼是否一致
        if password != password_confirm:
            messages.error(request, "密碼與確認密碼不一致")
            return redirect('register')  # 重定向回註冊頁面

        # 檢查電子郵件是否已存在
        if UserAccount.objects.filter(email=email).exists():
            messages.error(request, "該電子郵件已經被註冊")
            return redirect('register')  # 重定向回註冊頁面

        # 檢查使用者名稱是否已存在
        if UserAccount.objects.filter(username=username).exists():
            messages.error(request, "該使用者名稱已經被註冊")
            return redirect('register')

        # 創建新使用者
        new_user = UserAccount(username=username, email=email)
        new_user.set_password(password)  # 使用 set_password 方法加密密碼
        new_user.save()  # 儲存使用者資料到資料庫

        messages.success(request, "註冊成功，請登入")
        return redirect('login')  # 註冊成功後重定向到登入頁面

    return render(request, 'register.html',{'user':user})
def logout_user(request):
    logout(request)  # 清除 session，登出用戶
    return redirect('login')  # 登出後重定向到登入頁面

def profile(request):
    user=None
    user_id=request.session.get('user_id')

    from django.contrib.auth.hashers import make_password

def profile(request):
    user = None
    user_id = request.session.get('user_id')
    edit = request.GET.get('edit', 'false').lower() == 'true'
    history=request.POST.get('history')or "post"
    history_list=None
    print(history)
    if user_id:
        user = UserAccount.objects.get(id=user_id)
        if history=="comment":
            history_list=Comment.objects.filter(poster=user)
        else:
            history_list=Post.objects.filter(poster=user)
        # 檢查是否為 POST 請求，並更新使用者資料
     
        if request.method == 'POST' and not request.POST.get('history'):
            new_avatar=request.FILES.get('avatar')
            new_name = request.POST.get('username')
            current_password= request.POST.get('password')
            new_password = request.POST.get('new_password')
            comfirm_password= request.POST.get('comfirm_password')
            new_email = request.POST.get('email')
            
            if new_avatar:
                if user.avatar:
                    os.remove(user.avatar.path)  
                user.avatar=new_avatar
                    
            if new_name:
                user.username = new_name
            if new_email:
                user.email = new_email
            if new_password and new_password.strip():
                if not user.check_password(current_password):
                    messages.error(request,"舊密碼錯誤")
                    return HttpResponseRedirect("/auth/profile?edit=true")
                if  comfirm_password!=new_password:
                    messages.error(request,"兩次密碼不一致")
                    return HttpResponseRedirect("/auth/profile?edit=true")
                if  current_password==new_password:
                    messages.error(request,"舊密碼不可與新密碼相同")
                    return HttpResponseRedirect("/auth/profile?edit=true")
                user.set_password(new_password)
           
            

            user.save()  # 保存更改

            # 更新完成後可跳轉到某頁面或顯示成功訊息
            return HttpResponseRedirect('/auth/profile')

        return render(request, 'profile.html', {'user': user,'edit':edit,'history':history,'history_list':history_list})
    
    # 如未登入可跳轉至登入頁面
    return redirect('login')

    
