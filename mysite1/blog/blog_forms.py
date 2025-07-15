from django import forms
from .blog_models import Blog

class BlogForms(forms.ModelForm):
    #Meta클래스: 클래스in클래스
    class Meta:
        #DB에 전달해서 저장할내용만
        #fields에 있는 요소는 html의 form태그안에 name속성이 다 있어야함
        model = Blog
        fields = ['title', 'writer', 'contents']
        lables = {
            'title': '제목',
            'writer': '작성자',
            'contents': '내용'
        }
