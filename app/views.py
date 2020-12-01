from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView

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


class CustomerCreateView(CreateView):
    fields = '__all__'
    model = CustomerCompany
    template_name = 'customer_create.html'

# CBS for customer details, did not succeed in passing pk of customer to creation of new warehouse.
# #todo will try at a later point to make it work. Maybe workshop 3 will solve sth similar.
# class CustomerDetailView(DetailView):
#     model = CustomerCompany
#     context_object_name = 'customer'
#     template_name = 'customer_details.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # pk, user = self.kwargs['pk'], self.request.user
#         pk = self.kwargs['pk']
#         context['warehouse_list'] = Warehouse.objects.all().filter(customer_company=pk)
#         return context


class CustomerUpdateView(UpdateView):
    fields = '__all__'
    model = CustomerCompany
    template_name = 'customer_update.html'


class CustomerDeleteView(DeleteView):
    fields = '__all__'
    model = CustomerCompany
    template_name = 'customer_delete.html'
    success_url = reverse_lazy('customer list')


def details_or_add_warehouse(request, pk):
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
            warehouse = Warehouse(warehouse_address=form.cleaned_data['warehouse_address'])
            warehouse.customer_company = customer
            warehouse.save()
            return redirect('customer details', pk)
        context = {
            'customer': customer,
            'form': form,
        }


class TruckerListView(ListView):
    context_object_name = 'truckers'
    model = TransportCompany
    template_name = 'trucker_list.html'
