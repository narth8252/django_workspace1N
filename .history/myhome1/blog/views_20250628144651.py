#redirect는 기존걸 파괴시키고 클라이언트요청을 새로 받는것
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.
#HttpRequest -> 클라이언트가 보낸 정보를 받아오는 객체
#HttpResponse ->서버가 클라이언트로 보낼 정보를 저장해서
#               클라이언트에서 전달될 객체
#웹에서 정보를 요청하면 이 페이지가 호출됨

from .models import Blog
def index(request):
    return HttpResponse("Hello Django")
#쿼리 안만드는 장점이 있고 요즘 이게 대세임.
    # return HttpResponse("Hello Django");
#이 함수와 url을 연결하는 작업끝
#http://127.0.0.1/blog => blog.views.py파일의 index가 호출되게 한다.

def list(request):
    blog_list = Blog.objects.all()
    return render(request, "blog/blog_list.html", {"BlogList":blog_list})
    
from .forms import BlogForms
def write(request):
    form = BlogForms() #객체만들고
    return render(request, "blog/blog_write.html")

from django.utils import timezone
def save(request):
    #title = request.POST.get("title")
    form = BlogForms()
    blog = form.save(commit=False) #아직멈춤
    blog.wdate = timezone.now()  #wdate, hit태그는 안나와서 모델이 리턴.
    #timezone썼는데 주황줄뜨면 import해야됨.
    blog.hit=0
    blog.save()

    #글쓰기하고나면 목록화면으로 이동하는데
    #함수를 직접호출하지않고 클라이언트 통해서 다시 목록요청이 되게해야함
    #그것을 리다이렉트 path("list", views.list, name="list")라고 추가해놓으면 한바퀴돔.
    return redirect("blog:list")

def view(request, id):
    blog=Blog.objects.get(id=id) #DB에서 해당id읽어오기
    blog.hit 
    return render(request, "blog/blog_view.html", {"blog":blog})
                        # blog_view.html파일만들어서 화면에 뿌려주면됨.
    
    
