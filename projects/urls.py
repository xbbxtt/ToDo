from django.urls import path
from projects.views import (
    show_project_list,
    show_project_details,
    create_new_project,
)

urlpatterns = [
    path("", show_project_list, name="list_projects"),
    path("<int:id>/", show_project_details, name="show_project"),
    path("create/", create_new_project, name="create_project"),
]
