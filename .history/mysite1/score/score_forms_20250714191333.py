from django import forms
from .score_models import Score #form태그랑 model클래스연동

# Score 모델을 위한 ModelForm
class ScoreForm(forms.ModelForm):
    #내부클래스 
    class Meta:
        model = Score  # 연동할 모델 지정
        fields =['name', 'kor', 'eng', 'mat']
        labels = {
            'name':"이름",
            'kor':'국어',
            'eng':'영어',
            'mat':'수학',
        }
