from django.views.generic import TemplateView, RedirectView

from tracker.models import Task


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.exclude(is_deleted=True)
        return context

class IndexRedirectView(RedirectView):
    pattern_name = 'index'