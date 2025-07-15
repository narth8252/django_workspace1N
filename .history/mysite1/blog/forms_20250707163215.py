from django import forms
from blog.models import Blog

class BlogForms(forms.ModelForm):
    #Meta클래스: 클래스in클래스
    class Meta:
        model = Blog
        fields = [title, contents, writter]
        la
