from django import forms
from blog.models import Blog

#html -> form -> requset.POST.get[""]...
#html -> form -> model과 연동하는 파일만든다
#모델클래스랑 폼클래스 만든다.
class BlogForms(forms.ModelForm):
    class Meta:
        model = Blog #model과 form이 연동
        #insert into blog_blog(title, writer, contents)...
        fields = ['name', 'writer', 'contents']
        labels = {
            'title':'제목',
            'writer':"작성자",
            'contents':"내용"
        }
#