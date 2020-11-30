from django.urls import path

from app.views import LandingPage, OfferListView, MasterData, CustomerListView, TruckerListView, \
    CustomerCreateView, CustomerDeleteView, CustomerUpdateView, CustomerDetailView

urlpatterns = (
    path('', LandingPage.as_view(), name='landing page'),
    path('offers/', OfferListView.as_view(), name='offer list view'),
    path('master_data/', MasterData.as_view(), name='master data'),
    path('master_data/customers', CustomerListView.as_view(), name='customer list'),
    path('master_data/customers/create', CustomerCreateView.as_view(), name='customer create'),
    path('master_data/customers/details/<int:pk>', CustomerDetailView.as_view(), name='customer details'),
    path('master_data/customers/update/<int:pk>', CustomerUpdateView.as_view(), name='customer update'),
    path('master_data/customers/delete/<int:pk>', CustomerDeleteView.as_view(), name='customer delete'),
    path('master_data/truckers', TruckerListView.as_view(), name='trucker list'),
)
