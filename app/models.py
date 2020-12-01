from django.db import models
from django.urls import reverse


class Country(models.Model):
    name = models.CharField(max_length=20, blank=False)
    country_code = models.CharField(max_length=2, blank=False)

    def __str__(self):
        return f'{self.country_code} - {self.name}'


class Seaport(models.Model):
    name = models.CharField(max_length=20, blank=False)
    un_location_code = models.CharField(max_length=5, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.un_location_code} - {self.name}'


class CustomerCompany(models.Model):
    customer_name = models.CharField(max_length=20, blank=False)
    billing_address = models.CharField(max_length=40)
    company_logo = models.URLField
    published = models.BooleanField(default=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('customer list')

    def __str__(self):
        return f'{self.country} - {self.customer_name}'


class Warehouse(models.Model):
    warehouse_address = models.CharField(max_length=40, blank=False)
    ramp_on_site = models.BooleanField(default=False)
    customer_company = models.ForeignKey(CustomerCompany, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.country} / {self.customer_company} / {self.warehouse_address}'


class TransportCompany(models.Model):
    trucker_name = models.CharField(max_length=20, blank=False)
    billing_address = models.CharField(max_length=40)
    company_logo = models.URLField
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.country} - {self.trucker_name}'


class TransportRequest(models.Model):
    IMP = 'IMP'
    EXP = 'IMP'

    DIRECTIONS = (
        (IMP, 'Import'),
        (EXP, 'Export')
    )

    direction = models.CharField(max_length=20, choices=DIRECTIONS, blank=False)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    seaport = models.ForeignKey(Seaport, on_delete=models.CASCADE)

    def __str__(self):
        if self.direction == 'Import':
            return f'{self.warehouse.customer_company} ' \
                   f'requests move from {self.seaport.name} to {self.warehouse.warehouse_address}'
        else:
            return f'{self.warehouse.customer_company} ' \
                   f'requests move from {self.warehouse.warehouse_address} to {self.seaport.name}'


class TransportOffer(models.Model):
    rate = models.FloatField(blank=False)
    valid_from = models.DateField(blank=False)
    valid_to = models.DateField(blank=False)
    request = models.ForeignKey(TransportRequest, on_delete=models.CASCADE)
    trucker = models.ForeignKey(TransportCompany, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.rate} with {self.trucker.trucker_name} - ' \
               f'{self.request.warehouse.customer_company.customer_name} {self.request.__str__()} '
