from django.db import models

# Create your models here.
class Score(models.Model):
    name = models.CharField("이름", max_length=40)
    kor = m
