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
    tot = models.IntegerField("총점")