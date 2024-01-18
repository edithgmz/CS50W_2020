from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world!")
    # return HttpResponse("Hello!")
    return render(request, "hello/index.html")

def edith(request):
    return HttpResponse("Hello, Edith!")

def malu(request):
    return HttpResponse("Hello, Malu!")

def greet(request, name):
    # return HttpResponse(f"Hello, {name.capitalize()}!")
    return render(request, "hello/greet.html", {
        "name": name.capitalize
    })
