from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, DeleteView, UpdateView, DetailView

from exam_project.app.forms.transport_offer_form import TransportOfferForm
from exam_project.app.forms.transport_request_form import TransportRequestForm
from exam_project.app.models import TransportRequest, TransportOffer, Warehouse


class TransportRequestCreateView(LoginRequiredMixin, FormView):
    form_class = TransportRequestForm

    def form_valid(self, form):
        request = form.save(commit=False)
        request.user = self.request.user
        request.warehouse = Warehouse.objects.get(pk=self.kwargs['pk'])
        request.save()
        return redirect('warehouse details', self.kwargs['pk'])


class TransportRequestDeleteView(LoginRequiredMixin, DeleteView):
    fields = '__all__'
    model = TransportRequest
    template_name = 'request_delete.html'
    context_object_name = 'request'

    def get_success_url(self):
        request_to_delete_id = self.kwargs['pk']
        warehouse_id = TransportRequest.objects.get(pk=request_to_delete_id).warehouse.id
        return reverse_lazy('warehouse details', kwargs={'pk': warehouse_id})


class TransportRequestUpdateView(LoginRequiredMixin, UpdateView):
    form_class = TransportRequestForm
    model = TransportRequest
    context_object_name = 'request'
    template_name = 'request_update.html'

    def get_success_url(self):
        url = reverse_lazy('request details', kwargs={'pk': self.object.id})
        return url

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TransportRequestDetailsView(LoginRequiredMixin, DetailView):
    model = TransportRequest
    template_name = 'request_details.html'
    context_object_name = 'current_request'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        request = self.get_object()
        # admin = self.request.user.id == 1
        context['form'] = TransportOfferForm
        context['created_by'] = request.user
        context['offer_list'] = request.transportoffer_set.all()
        context['can_edit'] = self.request.user == request.user
        context['can_delete'] = self.request.user == request.user
        return context
