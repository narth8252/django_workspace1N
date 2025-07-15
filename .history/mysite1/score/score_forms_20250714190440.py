from django import form
from .score_models import Score #form태그랑 model클래스연동

class ScoreForm(forms.ModelForm):
    #내부클래스 
    class Meta:
        model = Score  # 사용할 모델 지정
        fields =['name', 'kor', 'eng', 'mat']
        labels = {
            'name':"이름",
            'kor':'국어',
            'eng':'영어',
            'mat':'수학',
        }
