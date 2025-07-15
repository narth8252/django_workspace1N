from django.db import models

# Create your models here.
#반드시 models.Model을 상속받아야 한다
#id필드는 자동으로 만든다
#ORM = 객체지향식 DB접근하려고 한다=쿼리 만들기싫어
#      단점: 테이블이 너무많고 join,서브쿼리 많을시 시간많이걸려 어려움
#테이블10개미만의 프로젝트생성시 매우 빠름.(하지만 이 경우 별로없음)
#Spring Entity가 여기 해당. 여기에 대응되는것이 Model클래스고 반드시 상속받아야함
#이 모델기반의 테이블만들고싶으면 settings.py파일에 

class Blog(models.Model):
    title = models.CharField("제목", max_length=200)
    contents = models.TextField("내용") #이건내용많으니 2GB까지 되는text필드로.
    writer = models.CharField("작성자", max_length=200)
    wdate = models.DateTimeField("작성일", auto_now=True) #바뀌는날짜 자동저장
    hit = models.IntegerField("조회수")

    #출력시 오더라이딩
    def __str__(self):
        return f"${self.title} ${self.writer}"