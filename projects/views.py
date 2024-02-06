from django.shortcuts import render, redirect
from projects.models import Project
from django.contrib.auth.decorators import login_required
from projects.forms import ProjectForm


# Create your views here.
@login_required
def show_project_list(request):
    list = Project.objects.filter(owner=request.user)
    context = {
        "project_list": list,
    }
    return render(request, "projects/project_list.html", context)


@login_required
def show_project_details(request, id):
    project = Project.objects.get(id=id)
    context = {"project_details": project}
    return render(request, "projects/details.html", context)


@login_required
def create_new_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()
    context = {
        "form": form,
    }
    return render(request, "projects/create_project.html", context)
