from django.views.generic import TemplateView
from .models import Portfolio


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['portfolios'] = Portfolio.objects.order_by('?').all()
        return context
