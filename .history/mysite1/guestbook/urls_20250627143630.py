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

    # path('sigma/<int:n>', views.sigma),
    path('sigma/<n>', views.sigma),
    path('isLeap', views.isLeap), #물음표는 없다는뜻이라 붙이지마.
    # path('calc/add/<int:x>/<int:y>', views.calc_add),
    # path('calc/sub/<int:x>/<int:y>', views.calc_sub),
    path("calc/<opcode>/<x>/<y>", views.calc)
    path("list", views.list)
    path("list", views.list)
    path("list", views.list)

]