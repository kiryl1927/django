from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
    context= {
        "zap": "text1",
        "zap2": "models.Model1.object.all()"

    }
    return render(request,"cat.html",context)

def about(request):
    return render(request,"about.html")

def dogs (request):
    return render(request,"dogs.html")

# Create your views here.
