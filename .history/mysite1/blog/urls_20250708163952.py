from django.contrib import admin
from django.urls import path
from . import views
#자기폴더에 있는 views.py를 찾아와라

#html에서 url 'blog:blog_view'
app_name="blog" #반드시필요

#config/urls.py파일의 모든요청을 받아서 분배
#config/urls.py파일에서 guestbook/urls.py를 찾을수있게
#config/urls.py  blog/~~~
# 콘피그폴더>urls.py로 잘찾아가서 수정해라.
app_name = "blog" #name반드시 필요함.
urlpatterns = [
    path("", views.index),
     path("list", views.getList2, name="blog_list2"),#json형식출력

    path("list", views.getList, name="blog_list"),
    path("write", views.write, name="blog_write"), #html페이지로 이동
    path("save", views.save, name="blog_save")  #데이터를 받아서 DB에 저장
]