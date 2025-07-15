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
문제2.http://127.0.0.1:8000/guestbook/isLeap?year=2025 윤년이면윤년,아니면윤년아님
문제3.http://127.0.0.1:8000/guestbook/calc/add/4/5 더하기연산결과
문제4.http://127.0.0.1:8000/guestbook/calc/sub/4/5 빼기연산결과
"""
#문제1./sigma/10 1~10까지 합계반환
def sigma(request, n):
    n = int(n)
    s=0
    for i in range(1, n+1)
    s+=i
    return HttpResponse({"result":s})

    

#문제2./isLeap?year=2025 윤년이면윤년,아니면윤년아님
def isLeap(request):
    year = request.GET.get("year")
    if year is None:
        return HttpResponse("year 파라미터:")
    year = int(year)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return HttpResponse("윤년")
    else:
        return HttpResponse("윤년아님")

#문제3./calc/add/4/5 더하기연산결과
def calc_add(request, x, y):
    result = int(x) + int(y)
    return HttpResponse(result)

#문제4./calc/sub/4/5 빼기연산결과
def calc_sub(request, x, y):
    result = int(x) - int(y)
    return HttpResponse(result)

