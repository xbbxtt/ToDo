from django.shortcuts import render, redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required
def show_project_list(request):
    list = Project.objects.filter(owner=request.user)
    context = {
        "project_list" : list,
    }
    return render(request, "projects/project_list.html", context)

@login_required
def show_project_details(request, id):
    project = Project.objects.get(id=id)
    context = {
        "project_details" : project
    }
    return render(request, "projects/details.html", context)
