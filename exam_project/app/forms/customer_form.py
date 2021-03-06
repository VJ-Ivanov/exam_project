from django import forms

from exam_project.app.models import CustomerCompany


class CustomerCompanyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = CustomerCompany
        fields = 'customer_name', 'billing_address', 'mark_up', 'country', 'published'

