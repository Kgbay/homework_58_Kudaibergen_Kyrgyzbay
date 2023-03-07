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


class TaskCreateView(TemplateView):
    template_name = 'task_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForm()
        return context

    def post(self, request, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            status = Status.objects.get(id=request.POST.get('status'))
            type = Type.objects.get(id=request.POST.get('type'))
            task = Task.objects.create(summary=form.cleaned_data['summary'],
                                       description=form.cleaned_data['description'],
                                       status=status, type=type)
            return redirect('task_view', pk=task.pk)
        return render(request, 'task_create.html',
                      context={'form': form})


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


class RemoveView(TemplateView):
    template_name = 'task_confirm_remove.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class ConfirmRemoveView(TemplateView):
    template_name = 'task_confirm_remove.html'

    def post(self, request, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        task.delete()
        return redirect('index')

