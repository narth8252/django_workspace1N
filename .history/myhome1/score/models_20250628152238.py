from django.db import models

# Create your models here.
class Score(models.Model):
    name = models.CharField("이름", max_length=40)
    kor = models.IntegerField("국어")
    eng = models.IntegerField("영어")
    mat = models.IntegerField("수학")
    wdate = models.DateTimeField(auto_now_add=True)
