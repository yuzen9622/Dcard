from django.db import models

# Create your models here.
class Post(models.Model):
    CATEGORY_CHOICES = [
        ('NTUB', '北商'),
        ('NTUT', '北科'),
        ('NTUH', '北醫'),
        ('NTUST', '台科'),
        ('other', '其他'),
        ('mood', '心情'),
        ('note', '雜記'),
        ('tech', '科技'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title