from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView, FormView

from app.forms.customer_form import CustomerCompanyForm
from app.forms.transport_offer_form import TransportOfferForm
from app.forms.transport_request_form import TransportRequestForm
from app.forms.warehouse_form import WarehouseForm
from app.models import TransportOffer, CustomerCompany, TransportCompany, Warehouse, TransportRequest


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


class CustomerCreateView(FormView):
    form_class = CustomerCompanyForm
    template_name = 'customer_create.html'
    success_url = reverse_lazy('customer list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CustomerUpdateView(UpdateView):
    form_class = CustomerCompanyForm
    model = CustomerCompany
    template_name = 'customer_update.html'
    success_url = reverse_lazy('customer list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class CustomerDeleteView(DeleteView):
    fields = '__all__'
    model = CustomerCompany
    template_name = 'customer_delete.html'
    success_url = reverse_lazy('customer list')


def customer_details_or_add_warehouse(request, pk):
    customer = CustomerCompany.objects.get(pk=pk)
    warehouse_list = Warehouse.objects.all().filter(customer_company=pk)

    if request.method == 'GET':
        context = {
            'customer': customer,
            'form': WarehouseForm(),
            'warehouse_list': warehouse_list
        }
        return render(request, 'customer_details.html', context)
    else:
        form = WarehouseForm(request.POST)
        if form.is_valid():
            warehouse = Warehouse(
                warehouse_address=form.cleaned_data['warehouse_address'],
                country=form.cleaned_data['country']
            )
            warehouse.customer_company = customer
            warehouse.save()
            return redirect('customer details', pk)


def warehouse_details_or_add_request(request, pk):
    current_warehouse = Warehouse.objects.get(pk=pk)
    order_list = TransportRequest.objects.all().filter(warehouse_id=pk)

    if request.method == 'GET':
        context = {
            'current_warehouse': current_warehouse,
            'form': TransportRequestForm(),
            'order_list': order_list
        }
        return render(request, 'warehouse_details.html', context)
    else:
        form = TransportRequestForm(request.POST)
        if form.is_valid():
            transport_request = TransportRequest(
                direction=form.cleaned_data['direction'],
                seaport=form.cleaned_data['seaport']
            )
            transport_request.warehouse = current_warehouse
            transport_request.save()
            return redirect('warehouse details', pk)


def transport_request_details_or_add_offer(request, pk):
    current_request = TransportRequest.objects.get(pk=pk)
    offer_list = TransportOffer.objects.all().filter(request_id=pk)

    if request.method == 'GET':
        context = {
            'current_request': current_request,
            'form': TransportOfferForm(),
            'offer_list': offer_list
        }
        return render(request, 'request_details.html', context)
    else:
        form = TransportOfferForm(request.POST)
        if form.is_valid():
            transport_offer = TransportOffer(
                rate=form.cleaned_data['rate'],
                valid_from=form.cleaned_data['valid_from'],
                valid_to=form.cleaned_data['valid_to'],
                trucker=form.cleaned_data['trucker'],
            )
            transport_offer.request = current_request
            transport_offer.save()
            return redirect('request details', pk)


class TruckerListView(ListView):
    context_object_name = 'truckers'
    model = TransportCompany
    template_name = 'trucker_list.html'
