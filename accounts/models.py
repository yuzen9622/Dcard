from django.db import models
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.
class UserAccount(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    avatar=models.ImageField(upload_to='avatars/',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def set_password(self, raw_password):
        self.password = make_password(raw_password)  # 使用 Django 的加密方式設置密碼

    # 自訂的方法來檢查密碼
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)  # 驗證密碼是否匹配

    def __str__(self):
        return self.username