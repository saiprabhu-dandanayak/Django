from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wish (request):
    wish = '<h1> Hello Everyone , This is SaiPrabhu  , currently learning Django</h1>'
    return  HttpResponse(wish)