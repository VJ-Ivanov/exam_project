from django.urls import path

from app.views import LandingPage, OfferListView, MasterData, CustomerListView, TruckerListView, \
    CustomerCreateView, CustomerDeleteView, CustomerUpdateView, customer_details_or_add_warehouse, \
    warehouse_details_or_add_request, transport_request_details_or_add_offer, TransportCompanyCreateView

urlpatterns = (
    path('', LandingPage.as_view(), name='landing page'),
    path('offers/', OfferListView.as_view(), name='offer list view'),
    path('master_data/', MasterData.as_view(), name='master data'),
    path('master_data/customers', CustomerListView.as_view(), name='customer list'),
    path('master_data/customers/create', CustomerCreateView.as_view(), name='customer create'),
    path('master_data/customers/details/<int:pk>', customer_details_or_add_warehouse, name='customer details'),
    path('master_data/customers/update/<int:pk>', CustomerUpdateView.as_view(), name='customer update'),
    path('master_data/customers/delete/<int:pk>', CustomerDeleteView.as_view(), name='customer delete'),
    path('master_data/warehouses/<int:pk>', warehouse_details_or_add_request, name='warehouse details'),
    path('master_data/requests/<int:pk>', transport_request_details_or_add_offer, name='request details'),
    path('master_data/truckers', TruckerListView.as_view(), name='trucker list'),
    path('master_data/truckers/create', TransportCompanyCreateView.as_view(), name='trucker create'),
)
