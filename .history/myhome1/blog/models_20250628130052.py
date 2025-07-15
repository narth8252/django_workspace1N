from django.db import models
#DB연동-스키마를 여기 정의하면 그대로 DB테이블생성
    #반드시 클래스로 상속받아야함.
    #ORM쿼리 기법
# Create your models here.
class Blog(models.Model):
    title = models.CharField("제목", max_length=200)
    contents = models.TextField("내용")
    wdate = models.DateTimeField("작성일", auto_now_add=True)
                                #객체생성시 자동날짜시간
    #null값허용 넣고
    writer = models.CharField("작성자", max_length=40, null=True, blank=True)
    hit = models.IntegerField("조회수", null=True, blank=True)
    hit = models.IntegerField("조", null=True, blank=True)
    hit = models.IntegerField("조회수", null=True, blank=True)

    #심플한 필드 만들어보고 DB랑 연동해보자.
# blog>models.py만들어서 class Blog 만들고, config>setting>인스톨앱아래 "blog.apps.BlogConfig",저장후 아래 실행
# (mysite)workspace1N>myhome1>python manage.py makemigrations
# 쌤PPT.52p

    #함수오버라이딩: 함수명이 같은데 매개변수가 다른것
    def __str__(self):
        return f"{self.title} {self.contents} {self.writer}"
        
