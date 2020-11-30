from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView

from app.models import TransportOffer, CustomerCompany, TransportCompany, Warehouse


class LandingPage(TemplateView):
    template_name = 'landing_page.html'


class MasterData(TemplateView):
    template_name = 'master_data.html'


class OfferListView(ListView):
    context_object_name = 'rates'
    model = TransportOffer
    template_name = 'rate_list.html'


class CustomerListView(ListView):
    context_object_name = 'customers'
    model = CustomerCompany
    template_name = 'customer_list.html'


class CustomerCreateView(CreateView):
    fields = '__all__'
    model = CustomerCompany
    template_name = 'customer_create.html'


class CustomerDetailView(DetailView):
    model = CustomerCompany
    context_object_name = 'customer'
    template_name = 'customer_details.html'


class CustomerUpdateView(UpdateView):
    fields = '__all__'
    model = CustomerCompany
    template_name = 'customer_update.html'


class CustomerDeleteView(DeleteView):
    fields = '__all__'
    model = CustomerCompany
    template_name = 'customer_delete.html'
    success_url = reverse_lazy('customer list')


class TruckerListView(ListView):
    context_object_name = 'truckers'
    model = TransportCompany
    template_name = 'trucker_list.html'
