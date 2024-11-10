from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category']
    def save(self, commit=True):
        # 獲取表單的實例
        post = super().save(commit=False)
        
        # 將 poster 設置為當前使用者
        post.poster = self.user  # 假設 `self.user` 是當前用戶

        # 如果需要立即保存，可以設置 commit=True
        if commit:
            post.save()
        return post