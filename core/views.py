from django.views.generic import FormView
from .models import Portfolio
from .forms import ContactForm
from django.contrib import messages
from django.urls import reverse_lazy
# from django.utils.translation import gettext as _
# from django.utils import translation


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['portfolios'] = Portfolio.objects.order_by('?').all()
        return context

    def form_valid(self, form, *args, **kwargs):
        content = {
                   'Name': form.cleaned_data['name'],
                   'E-mail': form.cleaned_data['email'],
                   'Message': form.cleaned_data['message']
                   }
        #
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Falha ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
