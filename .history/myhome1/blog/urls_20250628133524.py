from django.contrib import admin
from django.urls import path
from . import views
#자기폴더에 있는 views.py를 찾아와라


#config/urls.py파일의 모든요청을 받아서 분배
#config/urls.py파일에서 guestbook/urls.py를 찾을수있게
#config/urls.py  blog/~~~
# 콘피그폴더>urls.py로 잘찾아가서 수정해라.
urlpatterns = [
    path("", views.index),
    path("/l", views.index)
]