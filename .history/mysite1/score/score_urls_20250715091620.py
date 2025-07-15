from django.contrib import admin
from django.urls import path
from . import score_views  # 현재 앱(score) 안의 score_views.py 불러오기

# 앱 이름 설정 (URL Reverse 시 사용)
app_name = "score" #name반드시 필요함.

#config/urls.py파일의 모든요청을 받아서 분배
#config/urls.py파일에서 guestbook/urls.py를 찾을수있게
#config/urls.py  score/~~~
# 콘피그폴더>urls.py로 잘찾아가서 수정해라.

urlpatterns = [
    path("", score_views.index),  # /score/ 요청 시 index() 실행 → score_list로 redirect

    path("list", score_views.list, name="score_list"),  # /score/list → 전체 성적 목록
    path("view/<int:id>", score_views.view, name="score_view"),  # /score/view/3 → 개별 상세 보기
    path("write", score_views.write, name="score_write"),  # /score/write → 입력 폼
    path("save", score_views.save, name="score_save"),  # /score/save → POST 저장

    path("update/<int:id>", score_views.update, name="score_update"),  # /score/update/3 → 수정 처리
]