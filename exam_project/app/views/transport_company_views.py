from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView

from exam_project.app.forms.transport_company_form import TransportCompanyForm


class TransportCompanyCreateView(LoginRequiredMixin, FormView):
    form_class = TransportCompanyForm
    template_name = 'transport_company_create.html'
    success_url = reverse_lazy('trucker list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
