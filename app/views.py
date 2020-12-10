from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView, FormView

from app.forms.customer_form import CustomerCompanyForm
from app.forms.filter_form import FilterForm
from app.forms.transport_company_form import TransportCompanyForm
from app.forms.transport_offer_form import TransportOfferForm
from app.forms.transport_request_form import TransportRequestForm
from app.forms.warehouse_form import WarehouseForm
from app.models import TransportOffer, CustomerCompany, TransportCompany, Warehouse, TransportRequest


def extract_filter_values(params):
    order = params['order'] if 'order' in params else FilterForm.ORDER_ASC
    text = params['text'] if 'text' in params else ''

    return {
        'order': order,
        'text': text,
    }


class LandingPage(TemplateView):
    template_name = 'landing_page.html'


class MasterData(TemplateView):
    template_name = 'master_data.html'


class OfferListView(ListView):
    context_object_name = 'rates'
    model = TransportOffer
    template_name = 'rate_list.html'
    order_by_asc = True
    order_by = 'valid_to'
    contains_text = ''

    def dispatch(self, request, *args, **kwargs):
        params = extract_filter_values(request.GET)
        self.order_by = params['order']
        self.contains_text = params['text']
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        order_by = 'valid_to' if self.order_by == FilterForm.ORDER_ASC else '-valid_to'
        result = self.model.objects.filter(
            request__warehouse__customer_company__customer_name__icontains=self.contains_text
        ).order_by(order_by)
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = FilterForm(initial={
            'order': self.order_by,
            'text': self.contains_text
        })

        return context


class CustomerListView(LoginRequiredMixin, ListView):
    context_object_name = 'customers'
    model = CustomerCompany
    template_name = 'customer_list.html'


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
    template_name = 'customer_update.html'
    success_url = reverse_lazy('customer list')

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

    def dispatch(self, request, *args, **kwargs):
        customer = self.get_object()
        if customer.user_id != request.user.id:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


@login_required()
def customer_details_or_add_warehouse(request, pk):
    customer = CustomerCompany.objects.get(pk=pk)
    warehouse_list = Warehouse.objects.all().filter(customer_company=pk)
    admin = request.user.id == 1
    if request.method == 'GET':
        context = {
            'customer': customer,
            'form': WarehouseForm(),
            'warehouse_list': warehouse_list,
            'can_edit': request.user.userprofile.department == "Sales" or admin,
            'can_delete': request.user.userprofile.department == "Sales" or admin,
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
    admin = request.user.id == 1

    if request.method == 'GET':
        context = {
            'current_warehouse': current_warehouse,
            'form': TransportRequestForm(),
            'order_list': order_list,
            'can_edit': request.user.userprofile.department == "Sales" or admin,
            'can_delete': request.user.userprofile.department == "Sales" or admin,
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


class WarehouseDeleteView(LoginRequiredMixin, DeleteView):
    fields = '__all__'
    model = Warehouse
    template_name = 'warehouse_delete.html'

    def get_success_url(self):
        warehouse_to_delete_id = self.kwargs['pk']
        customer_id = Warehouse.objects.get(pk=warehouse_to_delete_id).customer_company.id
        return reverse_lazy('customer details', kwargs={'pk': customer_id})


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


class TransportCompanyCreateView(LoginRequiredMixin, FormView):
    form_class = TransportCompanyForm
    template_name = 'transport_company_create.html'
    success_url = reverse_lazy('trucker list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class TruckerListView(ListView):
    context_object_name = 'truckers'
    model = TransportCompany
    template_name = 'trucker_list.html'


# TODO How to add context to a CBS
# context["new_context_entry"] = new_context_entry
