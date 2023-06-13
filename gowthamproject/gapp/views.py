from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def name(request):
    n='<h1>hi this</h1>'
    return HttpResponse(n)
def child(request):
    return render(request,'gapp/ravi.html')
def spider(request):
    return render(request,'gapp/ravi.html')