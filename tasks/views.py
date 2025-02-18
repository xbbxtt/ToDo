from django.shortcuts import render, redirect
from tasks.models import Task
from django.contrib.auth.decorators import login_required
from tasks.forms import TaskForm


# Create your views here.
@login_required
def create_new_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = TaskForm()
    context = {
        "form": form,
    }
    return render(request, "tasks/create_task.html", context)


@login_required
def show_task_list(request):
    list = Task.objects.filter(assignee=request.user)
    context = {
        "task_list": list,
    }
    return render(request, "tasks/task_list.html", context)
