from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(requst):
    return HttpResponse("guestbook");

#GET방식이 파라미터 전달방식1
#x=1&y=1 파라미터
#http://127.0.0.1:8000/guestbook/test1?x=5&y=7
#url이 기억안나기때문에 꼬박꼬박 주석달아놓고 해라.
def test1(request):
    x = request.GET.get("x")
    y = request.GET.get("y")
    return HttpResponse(int(x)+int(y))