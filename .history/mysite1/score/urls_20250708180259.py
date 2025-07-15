from django.contrib import admin
from django.urls import path
from . import views
#자기폴더에 있는 views.py를 찾아와라

#html에서 url 'score:score_view'
app_name="score" #반드시필요

#config/urls.py파일의 모든요청을 받아서 분배
#config/urls.py파일에서 guestbook/urls.py를 찾을수있게
#config/urls.py  score/~~~
# 콘피그폴더>urls.py로 잘찾아가서 수정해라.
app_name = "score" #name반드시 필요함.
urlpatterns = [
    path("", views.index),
    path("list", views.getList, name="score_list"), #html
    path("view/<int:id>", views.view, name="score_view"), 
    path("write", views.write, name="score_write"), #html페이지로 이동
    path("save", views.save, name="score_save")  #데이터를 받아서 DB에 저장
]