from django.shortcuts import render
from projects.models import Project

# Create your views here.
def show_project_list(request):
    list = Project.objects.all()
    context = {
        "project_list" : list,
    }
    return render(request, "projects/project_list.html", context)
