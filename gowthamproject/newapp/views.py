from django.shortcuts import render
from django.http import HttpResponse
import datetime
def name(request):
    n=datetime.datetime.now()
    result='<h1> Time : '+str(n)+'</h1>'
    return HttpResponse(result)

# Create your views here.
