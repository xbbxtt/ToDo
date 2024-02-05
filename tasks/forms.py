from django.forms import ModelForm
from django import forms
from tasks.models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = (
            "name",
            "start_date",
            "due_date",
            "project",
            "assignee",
        )
        widgets = {
            'start_date':forms.TextInput(attrs={'type':'datetime-local'}),
            'due_date':forms.TextInput(attrs={'type':'datetime-local'}),
        }
