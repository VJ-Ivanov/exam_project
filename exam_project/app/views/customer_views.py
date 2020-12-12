from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from exam_project.app.forms.customer_form import CustomerCompanyForm
from exam_project.app.forms.warehouse_form import WarehouseForm
from exam_project.app.models import CustomerCompany


class CustomerCreateView(LoginRequiredMixin, CreateView):
    template_name = 'customer_create.html'
    model = CustomerCompany
    form_class = CustomerCompanyForm

    def get_success_url(self):
        url = reverse_lazy('customer details', kwargs={'pk': self.object.id})
        return url

    def form_valid(self, form):
        customer = form.save(commit=False)
        customer.user = self.request.user
        customer.save()
        return super().form_valid(form)


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    form_class = CustomerCompanyForm
    model = CustomerCompany
    context_object_name = 'customer'
    template_name = 'customer_update.html'
    # success_url = reverse_lazy('customer list')

    def get_success_url(self):
        url = reverse_lazy('customer details', kwargs={'pk': self.object.id})
        return url

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomerCompany
    template_name = 'customer_delete.html'
    success_url = reverse_lazy('customer list')
    context_object_name = 'customer'

    def dispatch(self, request, *args, **kwargs):
        customer = self.get_object()
        if customer.user_id != request.user.id:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class CustomerDetailsView(LoginRequiredMixin, DetailView):
    model = CustomerCompany
    template_name = 'customer_details.html'
    context_object_name = 'customer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.get_object()
        # admin = self.request.user.id == 1
        context['form'] = WarehouseForm
        context['created_by'] = customer.user
        context['warehouse_list'] = customer.warehouse_set.all()
        context['can_edit'] = self.request.user == customer.user
        context['can_delete'] = self.request.user == customer.user
        return context
