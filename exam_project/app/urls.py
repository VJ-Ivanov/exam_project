from django.urls import path

from exam_project.app.views.general_views import *
from exam_project.app.views.list_views import *
from exam_project.app.views.customer_views import *
from exam_project.app.views.warehouse_views import *
from exam_project.app.views.transport_request_views import *
from exam_project.app.views.transport_offer_views import *
from exam_project.app.views.transport_company_views import *

urlpatterns = (
    path('', LandingPage.as_view(), name='landing page'),
    path('offers/', OfferListView.as_view(), name='offer list view'),
    path('master_data/', MasterData.as_view(), name='master data'),
    path('customers', CustomerListView.as_view(), name='customer list'),
    path('customers/create', CustomerCreateView.as_view(), name='customer create'),
    # path('customers/details/<int:pk>', customer_details_or_add_warehouse, name='customer details'),
    path('customers/detail/<int:pk>', CustomerDetailsView.as_view(), name='customer details'),
    path('customers/update/<int:pk>', CustomerUpdateView.as_view(), name='customer update'),
    path('customers/delete/<int:pk>', CustomerDeleteView.as_view(), name='customer delete'),
    path('warehouse/create/<int:pk>', WarehouseCreateView.as_view(), name='warehouse create'),
    path('warehouses/<int:pk>', warehouse_details_or_add_request, name='warehouse details'),
    path('mwarehouses/delete/<int:pk>', WarehouseDeleteView.as_view(), name='warehouse delete'),
    path('requests/<int:pk>', transport_request_details_or_add_offer, name='request details'),
    path('truckers', TruckerListView.as_view(), name='trucker list'),
    path('truckers/create', TransportCompanyCreateView.as_view(), name='trucker create'),
)
