from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(requst):
    return HttpResponse("guestbook");

#x=1&y=1 파라미터
#http://127.0.0.1:8000/guestbook/test1?x=1&y=1
def test1(request):
    