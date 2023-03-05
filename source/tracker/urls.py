from django.urls import path

from .views.base import index_view
from .views.tasks import add_view, task_view, remove_view, task_confirm_remove, task_update_view

urlpatterns = [
    path("", index_view, name='index'),
    path("task/add/", add_view, name='task_add'),
    path("tasks/<int:pk>/", task_view, name='task_view'),
    path("tasks/<int:pk>/remove/", remove_view, name='remove_task'),
    path("tasks/<int:pk>/confirm_remove/", task_confirm_remove, name='confirm_remove_task'),
    path("tasks/<int:pk>/update/", task_update_view, name="update_task")
]