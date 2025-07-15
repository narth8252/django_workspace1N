from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator  # Paginator import
from .score_models import Score
from .score_forms import ScoreForms

# (중복 import는 제거 가능)
# from .models import Score

def index(request): 
    return redirect("score:score_list")
def list(request):  # 데이터 여러개 가져오기
    scoreList = Score.objects.all().order_by('-id')  # 최신 데이터가 먼저 오도록 정렬

    # 1. Paginator 객체 생성
    # 첫 번째 인자: 페이지화 쿼리셋 (scoreList)
    # 두 번째 인자: 한 페이지에 보여줄 객체 수 (예: 10개)
    paginator = Paginator(s
def getList(request):  #데이터 여러개 가져오기 # 리스트 조회
    scoreList = Score.objects.all()
    return render(request, "score/score_list.html",
                  {"scoreList": scoreList, "title": "성적처리"})

def view(request, id):  # 데이터 한개 가져오기
    scoreModel = get_object_or_404(Score, pk=id)
    return render(request, "score/score_view.html", {'item': scoreModel})

def write(request):
    scoreform = ScoreForms()
    # form객체를 만들어서 키값이 form이어야 한다
    # modify -> score_write.html 페이지를 등록으로도 쓰고 수정용으로도 쓰려고 한다
    context = {'form': scoreform,
               'modify': False}  # 추가하고자 하는 정보가 있으면 계속 추가하면 된다.
    return render(request, "score/score_write.html", context)



def save(request): #데이터 저장
    #csrf - 정상적인 로그인을 납치해서 다른사이트에서 침입한다. 미들웨어
    #방지하기위해 html파일을 get방식으로 부를때 csrf_token을 보내고있다.
    #restpul api말고(html없이 데이터만 주고받는 서버: html이 없으니 납치도못함)
    #미들웨어middleware:중간에 계속적인보안 = java의 필터체인 , config<settings에 알아서 만들어놈
    if request.method == "POST":
        # name = request.POST.get("name") #이부분일일히쓰기 귀찮으니 form.py클래스만들어서 떠넘김
        # pass #쓰다가 에러나면 pass써놓고 작업
        scoreform = ScoreForms(request.POST)
        scoreModel = scoreform.save(commit=False)
        #save를 저장하는시점에 form → model로 전환되어 온다.
        scoreModel.total = scoreModel.kor + scoreModel.eng + scoreModel.mat
        scoreModel.avg = scoreModel.total/3
        scoreModel.wdate = timezone.now()
        scoreModel.save() #프레임워크 단점은 프로그래머 의사를 제한
    return redirect("score:score_list")

# def update(save):
#     if

#     else:
#         # form = ScoreForms(instance=scoreModel)

#         return render

