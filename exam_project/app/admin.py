from django.contrib import admin
from django.contrib.admin import ModelAdmin, DateFieldListFilter

from exam_project.app.models import Country, Seaport, CustomerCompany, Warehouse, \
    TransportCompany, TransportRequest, TransportOffer


class WarehouseInLine(admin.StackedInline):
    model = Warehouse


class TransportRequestInline(admin.StackedInline):
    model = TransportRequest


class TransportOfferInline(admin.StackedInline):
    model = TransportOffer


class CustomerCompanyAdmin(ModelAdmin):
    list_display = ('id', 'customer_name', 'billing_address', 'country', 'user')
    inlines = (WarehouseInLine,)
    list_filter = ('country',)


class WarehouseAdmin(ModelAdmin):
    list_display = ('id', 'country', 'customer_company', 'warehouse_address', 'user')
    inlines = (TransportRequestInline,)
    list_filter = ('country', 'user')


class TransportRequestAdmin(ModelAdmin):
    list_display = ('id', 'direction', 'warehouse', 'seaport', 'user')
    inlines = (TransportOfferInline,)
    list_filter = ('direction', 'seaport', 'user')


class TransportOfferAdmin(ModelAdmin):
    list_display = ('id', 'request', 'rate', 'valid_from', 'valid_to', 'user')
    list_filter = ('valid_from', 'valid_to', 'user', )


admin.site.register(Country)
admin.site.register(Seaport)
admin.site.register(CustomerCompany, CustomerCompanyAdmin)
admin.site.register(Warehouse, WarehouseAdmin)
admin.site.register(TransportCompany)
admin.site.register(TransportRequest, TransportRequestAdmin)
admin.site.register(TransportOffer, TransportOfferAdmin)
