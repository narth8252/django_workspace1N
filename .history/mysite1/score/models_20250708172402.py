from django.db import models
# (base) C:\django_workspace1N>conda activate mysite
# (mysite) C:\django_workspace1N>cd mysite1
# (mysite) C:\django_workspace1N\mysite1>django-admin startapp score
# (mysite) C:\django_workspace1N\mysite1>
#무조건 models.Model을 상속받아야하고 id필드는 자동생성이므로 바꾸면X
class Score(models.Model):
    name = models.CharField("이름", max_length=40)
    kor = models.IntegerField("국어")
    eng = models.IntegerField("영어")
    mat = models.IntegerField("수학")
    tot = models.FloatField("평균")
    wdate = models.DateField("작성일", auto_created=True)
    #python manage.py makemigrations 실행하면 DB에 테이블을 생성할 파이썬코드 자동생성
    