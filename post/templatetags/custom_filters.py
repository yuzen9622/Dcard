# custom_filters.py
from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def time_since_custom(value):
    now = timezone.now()
    diff = now - value

    days = diff.days
    seconds = diff.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    if days > 0:
        return value.strftime('%Y年%m月%d日')
    elif hours > 0:
        return f"{hours}小時前"
    elif minutes > 0:
        return f"{minutes}分前"
    else:
        return "剛剛"
@register.filter
def time(value):
    now = timezone.now()
    diff = now - value

    days = diff.days
    seconds = diff.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    # 顯示像 2020年2月4日 19:47 這樣的格式
    return value.strftime('%Y年%m月%d日 %H:%M')
 
