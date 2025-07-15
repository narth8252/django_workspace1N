from django.contrib import admin
from django.urls import path
from . import views
#자기폴더에 있는 views.py를 찾아와라

app_name="blog" #반드시 해줘야 에러안남.

#config/urls.py파일의 모든요청을 받아서 분배
#config/urls.py파일에서 guestbook/urls.py를 찾을수있게
#config/urls.py  blog/~~~
# 콘피그폴더>urls.py로 잘찾아가서 수정해라.
urlpatterns = [
    path("", views.index), #blog/ 호출된다.
    path("list", views.list, name="list"), #request통해 가야함.새로고침누르면 추가등록 계속됨
    path("view/<int:id>", views.view, name="view"), #name에 넣어주면 이걸로 올수있음.
    path("write", views.write, name=""),
    path("save", views.save)
]