from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

#HttpRequest -> 클라이언트가 보낸 정보를 받아오는 객체
#HttpResponse ->서버가 클라이언트로 보낼 정보를 저장해서
#               클라이언트에서 전달될 객체
#웹에서 정보를 요청하면 이 페이지가 호출됨
def index():
    return H