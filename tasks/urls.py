from django.urls import path
from tasks.views import create_new_task


urlpatterns = [
    path("create/", create_new_task, name = "create_task"),
]
