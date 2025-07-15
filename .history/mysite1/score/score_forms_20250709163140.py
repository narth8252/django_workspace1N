from django import forms
from .models import Score #form태그랑 model클래스연동

class ScoreForms(forms.ModelForm):
    #Meta클래스: 클래스in클래스(내부클래스): 폼안에 있는거라 메타클래스안에 라벨넣어주
    class Meta:
        #DB에 전달해서 저장할내용만
        #fields에 있는 요소는 html의 form태그안에 name속성이 다 있어야함
        model = Score #defalt값인 model변수
        fields = ['name', 'kor', 'eng', 'mat']
        lables = {
            'name': '이름',
            'kor': '국어',
            'eng': '영어',
            'mat': '수학'
        }
