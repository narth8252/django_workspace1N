"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
# from blog import views #이건 첨에 해본거고
#외부에서 붙여올때는 이렇게 include(import같음)
#blog패키지로부터 views.py로딩
# from blog import views

#path중요
urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
    path("guestbook/", include("guestbook.urls"))
    # path("blog/", views.index) 
    #path함수가 url http://127.0.0.1:8000/blog
    #-->blog/views.py파일의 index함수를 연동.
]
#config/urls.py파일에서 guestbook/urls.py를 찾을수있게
#config폴더>urls.py로 잘찾아가서 수정해라.여러폴더에 동일한파일명有