from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

def isface(request):

    obj = {'res':'True'}
    #return HttpResponse("<em>Test</em>")
    data = json.dumps(obj)
    return HttpResponse(data,content_type='application/json')

def homePage(request):
    return HttpResponse("WELCOME TO HOMEPAGE")
