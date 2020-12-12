from django.shortcuts import render, redirect
from exam_project.app.forms.transport_offer_form import TransportOfferForm
from exam_project.app.models import TransportRequest, TransportOffer


def transport_request_details_or_add_offer(request, pk):
    current_request = TransportRequest.objects.get(pk=pk)
    offer_list = TransportOffer.objects.all().filter(request_id=pk)

    if request.method == 'GET':
        context = {
            'current_request': current_request,
            'form': TransportOfferForm(),
            'offer_list': offer_list
        }
        return render(request, 'request_details.html', context)
    else:
        form = TransportOfferForm(request.POST)
        if form.is_valid():
            transport_offer = TransportOffer(
                rate=form.cleaned_data['rate'],
                valid_from=form.cleaned_data['valid_from'],
                valid_to=form.cleaned_data['valid_to'],
                trucker=form.cleaned_data['trucker'],
            )
            transport_offer.request = current_request
            transport_offer.save()
            return redirect('request details', pk)