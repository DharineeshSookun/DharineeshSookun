from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(response):
	return HttpResponse("Homepage webcup")

def home(response):
	return render(response, "main/home.html")