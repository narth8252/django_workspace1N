from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse, JsonResponse
# Create your views here.

#HttpRequest -> 클라이언트가 보낸 정보를 받아오는 객체
#HttpResponse ->서버가 클라이언트로 보낼 정보를 저장해서
#               클라이언트에서 전달될 객체
#웹에서 정보를 요청하면 이 페이지가 호출됨
from blog.blog_models import Blog
def index(request):
    return HttpResponse("Hello Django");

#이 함수와 url을 연결하는 작업필요
#http://127.0.0.1/blog => blog.views.py파일의 index가 호출되게 한다.

from django.core import serializers

#http://127.0.0.1:8000/blog/list
def getList2(request):
    dataSet = list(Blog.objects.values())
    #직렬화 - 객체를 파일이나 네트워크로 출력하고자 하는걸 직렬화
    #data = serializers.serialize("json", dataSet)
    return JsonResponse(dataSet, safe=False, json_dumps_params={'ensure_ascii': False})

def getList(request):
    dataSet = list(Blog.objects.values())
    #직렬화 - 객체를 파일이나 네트워크로 출력하고자 하는걸 직렬화
    #data = serializers.serialize("json", dataSet)
    return render(request, "blog/blog_list.html", {"blogList":dataSet})

def view(request, id):  #blog/폴더아래 blog_view.html페이지로 이동
    # print("id = ", id)
    # sql = "select * from blog_blog where id=" +str(id) #직접안하겠다
    blog = Blog.objects.get(id=id) #키=키값
    return render(request, "blog/blog_view.html", {"blog":blog})

def write(request):  #blog/폴더아래 blog_write.html페이지로 이동
    return render(request, "blog/blog_write.html")

#. 은 나랑같은 디렉토리, forms파일명.py, BlogForms클래스 가져온다
from .blog_forms import BlogForms
from django.utils import timezone
from django.shortcuts import redirect

def save(request):  #blog/폴더아래 blog_write.html페이지로 이동
    form = BlogForms(request.POST) #form.fieldList에 있는 title에 form태그의 title값들어온다
    blogModel = form.save(commit=False) #DB저장끝났지만 완료는아님
    #리턴이 모델반환
    blogModel.wdate = timezone.now()
    blogModel.hit = 0
    blogModel.save() #확정하기

    #마지막으로 저장하고나면 글목록list로 이동하는데
    #절대로 직접 blog_list 메서트호출하면안됨. 
    #글등록후 request객체 
    #내부적으로 send redirect라는 게 정리작업해야하는데 -> 클라이언트로부터 다시 list 요청이 온것처럼 함
    return redirect("blog:blog_list") 
        # blog:blog_list → app name등록 blog, name="blog_list"




