from django.shortcuts import render, get_object_or_404
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Task

class NewTaskForm(forms.ModelForm):
    class Meta: 
        model = Task
        fields = ['task']

def index(request):
    tasks = Task.objects.all()
    return render(request, "task/index.html", {
        "tasks": tasks
    })
# Add a new task:
def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("task:index"))
        else:
            return render(request, "task/add.html", {
                "form": form
            })
        

    return render(request, "task/add.html", {
        "form": NewTaskForm()
    })

def complete_task(request, task_id): 
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return HttpResponseRedirect(reverse("task:index"))

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return HttpResponseRedirect(reverse("task:index"))

def edit_task(request, task_id):
    task = get_object_or_404(Task,id=task_id)
    if request.method == "POST":
        form = NewTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("task:index"))
    else:
        form = NewTaskForm(instance=task)
    return render(request, "task/edit.html", {
        "form": form, 
        "task_id": task_id
    })
        

