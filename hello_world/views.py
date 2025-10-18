from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    output = ""
    for i in range(1,10):
        output += "<p>" + str(i) + "</p>"
    return HttpResponse(output)
