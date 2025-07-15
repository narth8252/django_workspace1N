from django.db import models

#무조건 models.Model을 상속받아야하고 id필드는 자동생성이므로 바꾸면X
class Score(models.Model):