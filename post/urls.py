from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("category/",views.post_list,name="post_list"),
    path("category/<str:category>/",views.post_list,name="post_list_by_category"),
    path('create/', views.post_create, name='post_create'),
    path('article/<int:id>/',views.article_post,name="article_post"),
    path('search/',views.search_post,name="search_post"),
    path('comment/',views.comment_post,name="comment_post"),
    path('comment_delete/<int:id>',views.comment_delete,name="comment_delete"),
    path('comment_edit/<int:id>',views.comment_edit,name="comment_edit"),
]