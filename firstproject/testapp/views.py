import datetime

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def display(request):
    s = '<h1>Hello Everyone this is Prabhu</h1>'
    return HttpResponse(s)

def time(request):
    time=datetime.datetime.now()
    s='<h1>Hello Current Date and Time is :'+str(time)+'</h1>'
    return HttpResponse(s)

def good_morning(request):
    s = '<h1>Good Morning! Have a great day ahead.</h1>'
    return HttpResponse(s)

def good_afternoon(request):
    s = '<h1>Good Afternoon! Hope you\'re having a wonderful day.</h1>'
    return HttpResponse(s)

def good_evening(request):
    s = '<h1>Good Evening! Relax and enjoy the rest of your day.</h1>'
    return HttpResponse(s)


def greeting_based_on_time(request):
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        greeting = "Good Morning!"
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"

    html = f"<h1>{greeting} This is Prabhu.</h1>"
    return HttpResponse(html)