from django.shortcuts import render
from django.http import HttpResponse
from math import factorial

def index(request):
    return HttpResponse("<h1>Welcome to app</h1>")

def home(request):
    return render(request, "myapp/home.html", {'name' : 'Bhavaikya'})

def fact(request,n):
    n = int(n)
    return HttpResponse("<h4>Factorial is {}</h4>".format(factorial(n)))

def child(request):
    return render(request, "child.html")

def sam(request):
    return render(request, "myapp/sample.html", {'name' : 'Bhav'})




