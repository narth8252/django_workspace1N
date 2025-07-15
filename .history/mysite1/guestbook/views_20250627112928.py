from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(requst):
    return HttpResponse("guestbook");

#GET방식이 파라미터 전달방식1.
#x=1&y=1 파라미터
#http://127.0.0.1:8000/guestbook/test1?x=5&y=7
#url이 기억안나기때문에 꼬박꼬박 주석달아놓고 해라.
def test1(request):
    x = request.GET.get("x")
    y = request.GET.get("y")
    return HttpResponse(int(x)+int(y))

#GET방식이 파라미터 전달방식2.요즘권장코드
#/4/5 파라미터
#http://127.0.0.1:8000/guestbook/test2/5/7
def test2(request, x, y):
    return HttpResponse(int(x)+int(y))

def test3(request):
    if request.method=="POST":
        x = request.POST.get("x")
        y = request.POST.get("y")
        return HttpResponse(int(x)+int(y))
    else:
        return HttpResponse("Error")
    
"""
250627 AM11시 문제
문제1.http://127.0.0.1:8000/guestbook/sigma/10 1~10까지 합계반환
문제2.http://127.0.0.1:8000/guestbook/isLeap?year
"""