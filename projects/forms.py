from django.forms import ModelForm
from django import forms
from projects.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = (
            "name",
            "description",
            "owner",
        )
