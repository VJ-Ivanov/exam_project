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
    path('customers/detail/<int:pk>', CustomerDetailsView.as_view(), name='customer details'),
    path('customers/update/<int:pk>', CustomerUpdateView.as_view(), name='customer update'),
    path('customers/delete/<int:pk>', CustomerDeleteView.as_view(), name='customer delete'),

    path('warehouses/create/<int:pk>', WarehouseCreateView.as_view(), name='warehouse create'),
    path('warehouses/details/<int:pk>', WarehouseDetailsView.as_view(), name='warehouse details'),
    path('warehouses/update/<int:pk>', WarehouseUpdateView.as_view(), name='warehouse update'),
    path('warehouses/delete/<int:pk>', WarehouseDeleteView.as_view(), name='warehouse delete'),

    path('requests/create/<int:pk>', TransportRequestCreateView.as_view(), name='request create'),
    path('requests/details/<int:pk>', TransportRequestDetailsView.as_view(), name='request details'),
    path('requests/update/<int:pk>', TransportRequestUpdateView.as_view(), name='request update'),
    path('requests/delete/<int:pk>', TransportRequestDeleteView.as_view(), name='request delete'),

    path('offers/create/<int:pk>', TransportOfferCreateView.as_view(), name='offer create'),
    path('offers/details/<int:pk>', TransportOfferDetailsView.as_view(), name='offer details'),
    path('offer/update/<int:pk>', TransportOfferUpdateView.as_view(), name='offer update'),
    path('offer/delete/<int:pk>', TransportOfferDeleteView.as_view(), name='offer delete'),

    path('truckers', TruckerListView.as_view(), name='trucker list'),
    path('truckers/create', TransportCompanyCreateView.as_view(), name='trucker create'),
)
