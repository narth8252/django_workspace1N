from django.shortcuts import redirect, render
from django.utils import timezone
from django.http import HttpRequest, HttpResponse
from .models import Score

def index(request): 
    return redirect("score:score_list")

def getList(request): #데이터 여러개 가져오기
def getList(request):  # ← 이름 바꿔줌
    scoreList = Score.objects.all()
    return render(request, "score/score_list.html",
                  {"scoreList": scoreList, "title": "성적처리"})

def index(request, id): #데이터 한개 가져오기
    return render(request, "score/score_view.html")

def index(request): 
    return render(request, "score/score_write.html")

def save(request): #데이터 저장
    return redirect("score:score_list")
