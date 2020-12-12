from django import forms
from exam_project.app.models import Warehouse


class WarehouseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control form-control-sm'

    class Meta:
        model = Warehouse
        fields = 'warehouse_address', 'country', 'ramp_on_site'
