from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
import django_filters

from exam_project.app.forms.filter_form import FilterForm
from exam_project.app.models import TransportOffer, CustomerCompany, TransportCompany, TransportRequest


def extract_filter_values(params):
    order = params['order'] if 'order' in params else FilterForm.ORDER_ASC
    text = params['text'] if 'text' in params else ''

    return {
        'order': order,
        'text': text,
    }


class RateFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = TransportOffer
        fields = ['rate', 'valid_from', 'valid_to']


class OfferListView(ListView):
    context_object_name = 'rates'
    model = TransportOffer
    template_name = 'rate_list.html'
    order_by_asc = True
    order_by = 'valid_to'
    contains_text = ''

    def dispatch(self, request, *args, **kwargs):
        params = extract_filter_values(request.GET)
        self.order_by = params['order']
        self.contains_text = params['text']
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        order_by = 'valid_to' if self.order_by == FilterForm.ORDER_ASC else '-valid_to'
        result = self.model.objects.filter(
            request__warehouse__customer_company__customer_name__icontains=self.contains_text
        ).order_by(order_by)
        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = FilterForm(initial={
            'order': self.order_by,
            'text': self.contains_text
        })

        return context


class CustomerListView(LoginRequiredMixin, ListView):
    context_object_name = 'customers'
    model = CustomerCompany
    template_name = 'list_customers.html'


class TruckerListView(LoginRequiredMixin, ListView):
    context_object_name = 'truckers'
    model = TransportCompany
    template_name = 'trucker_list.html'


class OpenRequestListView(LoginRequiredMixin, ListView):
    model = TransportRequest
    template_name = 'list_requests_open.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        index_quotes = set([q.request.id for q in TransportOffer.objects.get_queryset()])
        context['open_requests'] = [r for r in self.model.objects.all() if r.id not in index_quotes]
        context['can_quote'] = self.request.user.userprofile.department == 'Pricing'
        return context
