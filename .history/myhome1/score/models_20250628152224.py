from django.db import models

# Create your models here.
class Score(models.Model):
    name = models.CharField("이름", max_length=40)
    kor = models.IntegerField("")
    eng = models.IntegerField("")
    kor = models.IntegerField("")
    wdate = models.DateTimeField(auto_now_add=True)
