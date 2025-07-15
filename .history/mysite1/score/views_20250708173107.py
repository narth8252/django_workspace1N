from django.shortcuts import render
from django.utils import timezone
from django.http import HttpRequest, HttpResponse

def index(request):
    return redirect("score")
