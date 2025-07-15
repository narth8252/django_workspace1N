from django.shortcuts import redirect, render
from django.utils import timezone
from django.http import HttpRequest, HttpResponse

def index(request): #
    return redirect("score:score_list")

def index(request): #데이터 여러개 가져오기
    return render(request, "score/score_list.html")

def index(request, id): #데이터 한개 가져오기
    return render(request, "score/score_view.html")

def index(request): #데이터 저장
    return render(request, "score/score_write.html")
