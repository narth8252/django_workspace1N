from django.db import models
#DB연동-스키마를 여기 정의하면 그대로 DB테이블생성
    #반드시 클래스로 상속받아야함.
# Create your models here.
class Blog(models.Model):
    title = models.CharField("제목", max_length=200)
    contents = models.TextField("내용")
    wdate = models.DateTimeField("작성일", auto_now_add=True)
                                #객체생성시 자동날짜시간
    #null값허용 넣고
    writer = models.CharField("작성자", max_length=40)
    hit = models.IntegerField

