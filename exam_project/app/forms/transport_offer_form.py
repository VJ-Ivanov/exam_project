from django import forms

from exam_project.app.models import TransportOffer


class DateInput(forms.DateInput):
    input_type = 'date'


class TransportOfferForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = TransportOffer
        fields = 'rate', 'valid_from', 'valid_to', 'trucker'
        widgets = {
            'valid_from': DateInput(),
            'valid_to': DateInput(),
        }
