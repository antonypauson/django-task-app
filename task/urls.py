from django.urls import path
from . import views

app_name = "task"
urlpatterns = [
    path("", views.index,name="index"),
    path("add/", views.add,name="add"),
    path("complete/<int:task_id>/", views.complete_task, name="complete_task"),
    path("delete/<int:task_id>/", views.delete_task, name="delete_task"),
    path("edit/<int:task_id>/", views.edit_task, name="edit_task"),
]