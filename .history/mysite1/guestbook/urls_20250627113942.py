from django.contrib import admin
from django.urls import path
from . import views

#config/urls.py파일의 모든요청을 받아서 분배
#config/urls.py파일에서 guestbook/urls.py를 찾을수있게
#config폴더>urls.py로 잘찾아가서 수정해라.
urlpatterns = [
    path("", views.index),
    path("test1", views.test1),
    path("test2/<x>/<y>", views.test2),
    #def test2(request, x, y) views.py에 쓴 변수명이 같아야함.
    path("test3", views.test3),
    
    path('sigma/<int:n>', views.sigma),
]
# ...existing code...
]