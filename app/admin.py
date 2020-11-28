from django.contrib import admin
from app.models import Country, Seaport, CustomerCompany, Warehouse, \
    TransportCompany, TransportRequest, TransportOffer

admin.site.register(Country)
admin.site.register(Seaport)
admin.site.register(CustomerCompany)
admin.site.register(Warehouse)
admin.site.register(TransportCompany)
admin.site.register(TransportRequest)
admin.site.register(TransportOffer)
