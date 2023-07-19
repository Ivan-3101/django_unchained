from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

tasks_list = ["check email","backup files","pray"]

def index(request):
    return render(request,"tasks/index.html",{
        "tasks":tasks_list,
    })

def ivan(request,name):
    return render(request,"tasks/ivan.html",{
        "name" :name.capitalize(), 
    })