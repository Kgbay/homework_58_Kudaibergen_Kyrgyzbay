from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from tracker.models import Task


def Index(request: WSGIRequest):
    tasks = Task.objects.exclude(is_deleted=True)
    context = {
        'tasks': tasks
    }
    return render(request, 'index.html', context=context)