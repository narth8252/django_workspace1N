from django.db import models
#DB연동-스키마를 여기 정의하면 그대로 DB테이블생성
    #반드시 클래스로 상속받아야함.
# Create your models here.
class Blog(models.Model):
    title = models.CharField("", max_length=200)
    contents = models.DateTimeField("작성일", auto_now_add=True)
