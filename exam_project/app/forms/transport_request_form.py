from django import forms
from exam_project.app.models import TransportRequest


class TransportRequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = TransportRequest
        fields = 'direction', 'seaport',
