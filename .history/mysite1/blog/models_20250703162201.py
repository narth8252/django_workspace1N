from django.db import models

# Create your models here.
#반드시 models.Model을 상속받아야 한다
#id필드는 자동으로 만든다
#ORM = 객체지향식 DB접근하려고 한다=쿼리 만들기싫어
class BlogModel(models.Model):
    title = models.CharField("제목", max_length=200)
    contents = models.textField("내용") #이건내용많으니 2GB까지 되는text필드로.
    writer = models.CharField("작성자", max_length=200)
    wdate = models.DateTimeField("작성일", max_length=200)
    title = models.CharField("제목", max_length=200)
    title = models.CharField("제목", max_length=200)
