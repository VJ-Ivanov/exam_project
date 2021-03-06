from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView, DeleteView, UpdateView, DetailView

from exam_project.app.forms.transport_request_form import TransportRequestForm
from exam_project.app.forms.warehouse_form import WarehouseForm
from exam_project.app.models import CustomerCompany, Warehouse, TransportRequest


class WarehouseCreateView(LoginRequiredMixin, FormView):
    form_class = WarehouseForm

    def form_valid(self, form):
        warehouse = form.save(commit=False)
        warehouse.user = self.request.user
        warehouse.customer_company = CustomerCompany.objects.get(pk=self.kwargs['pk'])
        warehouse.country = CustomerCompany.objects.get(pk=self.kwargs['pk']).country
        warehouse.save()
        return redirect('customer details', self.kwargs['pk'])


class WarehouseDeleteView(LoginRequiredMixin, DeleteView):
    fields = '__all__'
    model = Warehouse
    template_name = 'warehouse_delete.html'

    def get_success_url(self):
        warehouse_to_delete_id = self.kwargs['pk']
        customer_id = Warehouse.objects.get(pk=warehouse_to_delete_id).customer_company.id
        return reverse_lazy('customer details', kwargs={'pk': customer_id})


class WarehouseUpdateView(LoginRequiredMixin, UpdateView):
    form_class = WarehouseForm
    model = Warehouse
    context_object_name = 'warehouse'
    template_name = 'warehouse_update.html'

    def get_success_url(self):
        url = reverse_lazy('warehouse details', kwargs={'pk': self.object.id})
        return url

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class WarehouseDetailsView(LoginRequiredMixin, DetailView):
    model = Warehouse
    template_name = 'warehouse_details.html'
    context_object_name = 'current_warehouse'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        warehouse = self.get_object()
        # admin = self.request.user.id == 1
        context['form'] = TransportRequestForm
        context['created_by'] = warehouse.user
        context['transport_request_list'] = warehouse.transportrequest_set.all()
        context['can_manipulate'] = self.request.user == warehouse.user
        return context



#
# def warehouse_details_or_add_request(request, pk):
#     current_warehouse = Warehouse.objects.get(pk=pk)
#     order_list = TransportRequest.objects.all().filter(warehouse_id=pk)
#     admin = request.user.id == 1
#
#     if request.method == 'GET':
#         context = {
#             'current_warehouse': current_warehouse,
#             'form': TransportRequestForm(),
#             'order_list': order_list,
#             'can_edit': request.user.userprofile.department == "Sales" or admin,
#             'can_delete': request.user.userprofile.department == "Sales" or admin,
#         }
#         return render(request, 'warehouse_details.html', context)
#     else:
#         form = TransportRequestForm(request.POST)
#         if form.is_valid():
#             transport_request = TransportRequest(
#                 direction=form.cleaned_data['direction'],
#                 seaport=form.cleaned_data['seaport']
#             )
#             transport_request.warehouse = current_warehouse
#             transport_request.save()
#             return redirect('warehouse details', pk)