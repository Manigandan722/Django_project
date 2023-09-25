
from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return render(request,'login 2.html')


def welcome(request):
    welcome="<h1> Welcome to my website</h1>"
    return HttpResponse (welcome)
    