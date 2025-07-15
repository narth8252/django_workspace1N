from django.contrib import admin
from django.urls import path
from . import views
#자기폴더에 있는 views.py를 찾아와라

app_name="score" #반드시 해줘야 에러안남.

urlpatterns = [
    path("", views.index), #blog/ 호출된다.
    path("list", views.list, name="list"), #request통해 가야함.새로고침누르면 추가등록 계속됨
    path("view/<int:id>", views.view, name="view"), #name에 넣어주면 이걸로 올수있음.
    path("write", views.write, name="write"), 
    # <a href="{% url 'blog:write' %}">등록</a> 버튼식으로 하고싶으면 위에 name="write"써야함.
    path("save", views.save)
]