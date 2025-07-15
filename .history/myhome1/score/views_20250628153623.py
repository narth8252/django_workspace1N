from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
# Create your views here.
def index(requst):
    return HttpResponse("score")

def view(requst):
    return 