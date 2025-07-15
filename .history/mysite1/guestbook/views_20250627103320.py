from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(requst):
    return HttpResponse("guestbook");

#x=&y=1 파라미터
#http