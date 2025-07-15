from django.shortcuts import redirect, render
from django.utils import timezone
from django.http import HttpRequest, HttpResponse

def index(request): 
    return redirect("score:score_list")

def index(request):
    return render(request, "score/score_list.html")

def index(request, id):
    return render(request, "score/score_view.html")

def index(request):
    return render(request, "score/score_write.html")
