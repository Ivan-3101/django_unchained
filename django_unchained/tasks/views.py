from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

from django import forms

tasks_list = ["check email","backup files","pray"]

class NewTaskForm_classname(forms.Form):
    # ALL THE FIELDS ID LIKE THE USER TO HAVE
    task = forms.CharField(label="New Task :")


def index(request):
    return render(request,"tasks/index.html",{
        "tasks":tasks_list,
    })

def add(request):
    return render(request,"tasks/add.html",{
        "var_form": NewTaskForm_classname()
        # give this template access
        # to a variable called form which will be a new task form
    
        # now instead of using the html form syntax
        # we use this {{ var_form }}
    
    })

def ivan(request,name):
    return render(request,"tasks/ivan.html",{
        "name" :name.capitalize(), 
    })