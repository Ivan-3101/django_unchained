from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

from django import forms

tasks_list = ["check email","backup files","pray"]

class NewTaskForm_classname(forms.Form):
    # ALL THE FIELDS ID LIKE THE USER TO HAVE
    task = forms.CharField(label="New Task :")
    priority = forms.IntegerField(label="Priority :",min_value=1,max_value=10)

def index(request):
    return render(request,"tasks/index.html",{
        "tasks":tasks_list,
    })

def add(request):

    # adding server side validation
    # if we use post request method
    # that means we are submitting the form
    # and i now want to submit a new task
    if request.method == "POST":
        # processing the result of that request
        new_form = NewTaskForm_classname(request.POST)
        # request.POST contains all the data the user submitted when clicked on submit
        
        if new_form.is_valid():
            task = new_form.cleaned_data["task"]
            # new_form.cleaned_data gives access to all data the user submitted
            # ["task"] because it is used in NewFormclass

            # if form is valid
            # we take data from the form
            # get the task
            # save inside variable called task
            # and add to growing list
            tasks_list.append(task)

        # if form is not valid
        else:
            return render(request,"tasks/add.html",{
                "var_form" : new_form
            # But else if the form is not valid, what should we do instead?
            # 1:25:27
            # Well, then I should return the add.html file again. But instead of providing the form back to them, a new form back to them,
            # 1:25:35
            # I'm going to send back the existing form data back to them. So we can display information about any errors that might have come up as well.
            })

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