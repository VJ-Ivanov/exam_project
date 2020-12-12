from django.contrib import admin
from django.contrib.admin import ModelAdmin

from app.models import Country, Seaport, CustomerCompany, Warehouse, \
    TransportCompany, TransportRequest, TransportOffer


class WarehouseInLine(admin.StackedInline):
    model = Warehouse


class CustomerCompanyAdmin(ModelAdmin):
    list_display = ('id', 'customer_name', 'billing_address', 'country', 'user')
    inlines = (WarehouseInLine,)
    list_filter = ('country',)


class WarehouseAdmin(ModelAdmin):
    list_display = ('id', 'warehouse_address', 'customer_company')


admin.site.register(Country)
admin.site.register(Seaport)
admin.site.register(CustomerCompany, CustomerCompanyAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(TransportCompany)
admin.site.register(TransportRequest)
admin.site.register(TransportOffer)
