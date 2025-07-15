from django.shortcuts import render
from django.utils import timezone
from django.http import HttpRequest, HttpResponse

def index(request):
    return redirect("score:score_list")

def index(request):
    return render(request, "score/score_list.html")
