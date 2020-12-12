from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView, UpdateView, DeleteView

from exam_project.app.forms.transport_offer_form import TransportOfferForm
from exam_project.app.models import TransportRequest, TransportOffer


class TransportOfferCreateView(LoginRequiredMixin, FormView):
    form_class = TransportOfferForm

    def form_valid(self, form):
        offer = form.save(commit=False)
        offer.user = self.request.user
        offer.request = TransportRequest.objects.get(pk=self.kwargs['pk'])
        offer.save()
        return redirect('request details', self.kwargs['pk'])


class TransportOfferDetailsView(LoginRequiredMixin, DetailView):
    model = TransportOffer
    template_name = 'offer_details.html'
    context_object_name = 'current_offer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        offer = self.get_object()
        # admin = self.request.user.id == 1
        context['form'] = TransportOfferForm
        context['created_by'] = offer.user
        context['can_edit'] = self.request.user == offer.user
        context['can_delete'] = self.request.user == offer.user
        return context


class TransportOfferDeleteView(LoginRequiredMixin, DeleteView):
    # fields = '__all__'
    model = TransportOffer
    template_name = 'offer_delete.html'
    context_object_name = 'offer'

    def get_success_url(self):
        offer_to_delete_id = self.kwargs['pk']
        request_id = TransportOffer.objects.get(pk=offer_to_delete_id).request.id
        return reverse_lazy('request details', kwargs={'pk': request_id})


class TransportOfferUpdateView(LoginRequiredMixin, UpdateView):
    form_class = TransportOfferForm
    model = TransportOffer
    context_object_name = 'offer'
    template_name = 'offer_update.html'

    def get_success_url(self):
        url = reverse_lazy('offer details', kwargs={'pk': self.object.id})
        return url

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
