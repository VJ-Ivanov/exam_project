from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DeleteView, UpdateView, DetailView, FormView

from exam_project.app.forms.customer_form import CustomerCompanyForm
from exam_project.app.forms.filter_form import FilterForm
from exam_project.app.forms.transport_company_form import TransportCompanyForm
from exam_project.app.forms.transport_offer_form import TransportOfferForm
from exam_project.app.forms.transport_request_form import TransportRequestForm
from exam_project.app.forms.warehouse_form import WarehouseForm
from exam_project.app.models import TransportOffer, CustomerCompany, TransportCompany, Warehouse, TransportRequest


# @login_required()
# def customer_details_or_add_warehouse(request, pk):
#     customer = CustomerCompany.objects.get(pk=pk)
#     warehouse_list = Warehouse.objects.all().filter(customer_company=pk)
#     admin = request.user.id == 1
#     if request.method == 'GET':
#         context = {
#             'customer': customer,
#             'form': WarehouseForm(),
#             'warehouse_list': warehouse_list,
#             'can_edit': request.user.userprofile.department == "Sales" or admin,
#             'can_delete': request.user.userprofile.department == "Sales" or admin,
#         }
#         return render(request, 'customer_details.html', context)
#     else:
#         form = WarehouseForm(request.POST)
#         if form.is_valid():
#             warehouse = Warehouse(
#                 warehouse_address=form.cleaned_data['warehouse_address'],
#                 country=form.cleaned_data['country']
#             )
#             warehouse.customer_company = customer
#             warehouse.save()
#             return redirect('customer details', pk)










