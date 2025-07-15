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

from .models import Score

def save(request): #데이터 저장
    if request.method == "POST":
        # name = request.POST.get("name") #이부분일일히쓰기 귀찮으니 form.py클래스만들어서 떠넘김
        pass #쓰다가 에러나면 pass써놓고 작업
    return redirect("score:score_list")
