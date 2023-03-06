from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from tracker.models import Task, Type, Status, TypeChoice, StatusChoice
from tracker.forms import TaskForm


class TaskDetail(TemplateView):
    template_name = 'task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


# def add_view(request: WSGIRequest):
#     if request.method == "GET":
#         form = TaskForm()
#         return render(request,
#                       'task_create.html',
#                       context={
#                           'type_choices': TypeChoice.choices,
#                           'status_choices': StatusChoice.choices,
#                           'form': form,
#                       })
#
#     form = TaskForm(data=request.POST)
#     if not form.is_valid():
#         return render(request,
#                       'task_create.html',
#                       context={
#                           'type_choices': TypeChoice.choices,
#                           'status_choices': StatusChoice.choices,
#                           'form': form,
#                       })
#     else:
#         status = Status.objects.get(status_name=request.POST.get('status'))
#         type = Type.objects.get(type_name=request.POST.get('type'))
#         task = Task.objects.create(summary=form.cleaned_data['summary'], description=form.cleaned_data['description'], status=status, type=type)
#         return redirect('task_view', pk=task.pk)


class TaskCreateView(TemplateView):
    template_name = 'task_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForm()
        return context

    def post(self, request,  **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            status = Status.objects.get(id=request.POST.get('status'))
            type = Type.objects.get(id=request.POST.get('type'))
            task = Task.objects.create(summary=form.cleaned_data['summary'],
                                       description=form.cleaned_data['description'],
                                       status=status, type=type)
            return redirect('task_view', pk=task.pk)

class TaskUpdateView(TemplateView):
    template_name = 'task_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        context['form'] = TaskForm(instance=context['task'])
        return context

    def post(self, request, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_view', pk=task.pk)
        return render(request, 'task_update.html',
                      context={'form': form, 'task': task})

# def task_update_view(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     if request.method == 'GET':
#         form = TaskForm(initial={
#             'summary': task.summary,
#             'description':  task.description,
#             'type': task.type,
#             'status': task.status
#         })
#         return render(request, 'task_update.html', context={
#             'form': form,
#             'task': task
#         })
#
#
#     elif request.method == 'POST':
#         form = TaskForm(data=request.POST)
#         if form.is_valid():
#             task.summary = form.cleaned_data['summary']
#             task.description = form.cleaned_data['description']
#             status = Status.objects.get(status_name=request.POST.get('status'))
#             type = Type.objects.get(type_name=request.POST.get('type'))
#             task.status = status
#             task.type = type
#             task.save()
#             return redirect('task_view', pk=task.pk)
#         else:
#             return render(request, 'task_update.html', context={
#             'form': form,
#             'type_choices': TypeChoice.choices,
#             'status_choices': StatusChoice.choices
#         })


def remove_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_confirm_remove.html', context={'task': task})


def task_confirm_remove(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('index')
