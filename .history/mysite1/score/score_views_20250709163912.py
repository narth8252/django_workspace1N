from django.shortcuts import redirect, render
from django.utils import timezone
from django.http import HttpRequest, HttpResponse
from .score_models import Score

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

from .score_models import Score
from .score_forms import ScoreForm

def save(request): #데이터 저장
    #csrf - 정상적인 로그인을 납치해서 다른사이트에서 침입한다.
    #방지하기위해 html파일을 get방식으로 부를때 csrf_token을 보내고있다.
    #res
    if request.method == "POST":
        # name = request.POST.get("name") #이부분일일히쓰기 귀찮으니 form.py클래스만들어서 떠넘김
        # pass #쓰다가 에러나면 pass써놓고 작업
        Scoreform = ScoreForm(request.POST)
        ScoreModel = Scoreform.save(commit=False)
        #save를 저장하는시점에 form → model로 전환되어 온다.
        ScoreModel.total = ScoreModel.kor + ScoreModel.eng + ScoreModel.mat
        ScoreModel.avg = ScoreModel.total/3
        ScoreModel.wdate = timezone.now()
        ScoreModel.save() #프레임워크 단점은 프로그래머 의사를 제한
    return redirect("score:score_list")
