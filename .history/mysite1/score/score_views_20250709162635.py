from django.shortcuts import redirect, render
from django.utils import timezone
from django.http import HttpRequest, HttpResponse
from .models import Score

def index(request): 
    return redirect("score:score_list")

def getList(request):  #데이터 여러개 가져오기 # 리스트 조회
    scoreList = Score.objects.all()
    return render(request, "score/score_list.html",
                  {"scoreList": scoreList, "title": "성적처리"})

def view(request, id): #데이터 한개 가져오기
    return render(request, "score/score_view.html")

def write(request): 
    return render(request, "score/score_write.html")

def save(request): #데이터 저장
    if request.method == "POST"
    return redirect("score:score_list")
