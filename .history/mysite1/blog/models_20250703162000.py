from django.db import models

# Create your models here.
#반드시 models.Model을 상속받아야 한다
#id필드는 자동으로 만든다
#객체지향으로 만드려고 한다 -> OR
class BlogModel(models.Model):
    title = models.CharField("제목", max_length=200)
