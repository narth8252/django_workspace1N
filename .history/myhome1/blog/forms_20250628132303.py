from django import forms
from blog.models import Blog

#html -> form -> requset.POST.get[""]...
#html -> form -> model과 연동하는 파일만든다
class BlogForms(forms.ModelForm):
    class Mete:
        model = Blog #model과 form이 연동
        #insert into blog_blog(title, writer, contents)...
        fields = ['title', 'writer', 'contents']
        labels = {
            'title'
        }
#