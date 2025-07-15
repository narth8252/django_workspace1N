from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator # Paginator import
from .score_models import Score # Score 모델이 있다고 가정
from .score_forms import ScoreForm

# 페이지네이션 구성용 주석
#페이징??? << < 1 2 3 4 5 6 7 8 9 10 > >>
#DB로 데이터를 가져올 때 전부 갖고 오느냐 못 갖고 오느냐 판단된다
#페이징쿼리써서 원하는페이지의 데이터개수만큼 가져오기
#MySQL의 경우 limit 0,10 (10,10),(20,10),(30,10)
#전체페이지개수구해서 select count(*) from score_score
#페이지개수 구하기 totalPage = math.ceil(totalCnt/10)
#ORM지원하는 프레임워크들은 Paginator 거의다 지원
#page에 대한 정보를 저장할 클래스

def index(request): 
    return redirect("score:score_list")

def list(request): #데이터 여러개 가져오기
    scoreList = Score.objects.all().order_by('-id') # 최신 데이터가 먼저 오도록 정렬 (옵션)
    #DB에서 데이터를 전부 가져오게 설계
    #슬라이싱주면 limit 명령어로 전환돼 가져온다
    #쿼리가 모든데이터 가져와서 여기서 잘라냄. 5만개쯤 되면 객체로 못가져올가능성있다

    #1. 전체페이지개수: 데이터 전체개수 알아내고, 한페이지당 몇개씩 보일지 확인
#                   데이터 전체개수: 545, 한페이지당 10개씩 보겠다
#                   전체페이지수: 545/10 올림수 54.5 -> 올림수54 -> 54p이지만
#                               54.1,54...55.9까지 -> 55페이지
#                               math.ceiling함수쓰면 올림해줌
#                   << < 1 2 3 4 5 6 7 8 9 10 > >>
#                   << < 1 2 3 4 5 6 7 8 9 10 > >>
#                   < 이전페이지 이태그는 비활성화>
#                   > 이전페이지 이태그는 비활성화>
    
    # 1. Paginator 객체 생성
    # 첫 번째 인자: 페이징할 쿼리셋 (scoreList)
    # 두 번째 인자: 한 페이지에 보여줄 객체 수 (예: 10개)
    paginator = Paginator(scoreList, 10) # 한 페이지에 10개씩 보여줍니다.
    # 2. GET 요청에서 'page' 파라미터 값 가져오기
    # 요청에 'page' 파라미터가 없으면 기본값으로 1페이지를 보여줍니다.
    page_number = request.GET.get('page')
    #http://127.0.0.1:8000/score/list?page=1 urls.py파일에서
    #http://127.0.0.1:8000/score/list?page=2 
    # 3. 해당 페이지의 객체들 가져오기
    # page() 메소드는 해당 페이지의 Page 객체를 반환합니다.
    page_obj = paginator.get_page(page_number) 
    # 4. 템플릿으로 전달할 컨텍스트
    context = {
        "page_obj": page_obj, # Paginator가 반환한 Page 객체를 전달 (렌더링에 필요)
        "title": "성적처리",
        # 'scoreList': scoreList, # page_obj를 사용
    }
    return render(request, "score/score_list.html", context)

def getList(request):  #데이터 여러개 가져오기 # 리스트 조회
    scoreList = Score.objects.all()
    return render(request, "score/score_list.html",
                  {"scoreList": scoreList, "title": "성적처리"})

def view(request, id): #데이터 한개 가져오기
    scoreModel = get_object_or_404(Score, pk=id)
    #데이터 가져오기 get_object_or_404
    return render(request, "score/score_view.html", {'item':scoreModel})

def write(request):
    scoreform = ScoreForm() 
    #form객체를 만들어서 키값이 form이어야 한다 
    #modify-> score_write.html 페이지를 등록으로도 쓰고 수정으로도 쓰려고 한다 
    context ={'form':scoreform, 
              'modify':False} #추가하고자 하는 정보가 있으면 계속 추가하면 된다.
    return render(request, "score/score_write.html",context  )

def save(request): #데이터 저장
    #csrf - 정상적인 로그인을 납치해서 다른사이트에서 침입한다. 미들웨어
    #방지하기위해 html파일을 get방식으로 부를때 csrf_token을 보내고있다.
    #restpul api말고(html없이 데이터만 주고받는 서버: html이 없으니 납치도못함)
    #미들웨어middleware:중간에 계속적인보안 = java의 필터체인 , config<settings에 알아서 만들어놈
    if request.method =="POST":
        #name = request.POST.get("name")
        scoreform = ScoreForm(request.POST)
        scoreModel = scoreform.save(commit=False)
        #save를 저장하는 시점에서 form -> model 로 전환되서 온다 
        scoreModel.total = scoreModel.kor +scoreModel.eng + scoreModel.mat
        scoreModel.avg = scoreModel.total/3 
        scoreModel.wdate = timezone.now() 
        scoreModel.save() #프레임워크의 단점은 프로그래머 의사를 제한한다.  
    return redirect("score:score_list")

def update(request, id): #데이터저장
    print("id값 : ", id)
    scoreModel = get_object_or_404(Score, pk=id)
    print(scoreModel.name)
    if request.method=="POST":
        scoreform = ScoreForm(request.POST)
        scoreModel = scoreform.save(commit=False)
        scoreModel.total = scoreModel.kor +scoreModel.eng + scoreModel.mat
        scoreModel.avg = scoreModel.total/3 
        scoreModel.wdate = timezone.now() 
        scoreModel.save()
        return redirect("score:score_view", pk=scoreModel.id)
    else:
        form = ScoreForm(instance=scoreModel)
        print("name " , form)
    return render(request, 'score/score_write.html', {'form':form, 'modify':True, 'id':id})
