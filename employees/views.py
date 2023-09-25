from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import datetime

def gogd_mor(request):
    return HttpResponse('<h1>good morning</h1>')

def gogd_ev(request):
    return HttpResponse('<h1>good Evening</h1>')

def gogd_af(request):
    return HttpResponse('<h1>good Afternoon</h1>')
def time(request):
    time=datetime.datetime.now()
    result='<h1> the current time is :'+str(time)+'</h1>'
    return HttpResponse(result)

