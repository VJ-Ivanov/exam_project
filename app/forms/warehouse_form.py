from django import forms


class WarehouseForm(forms.Form):
    warehouse_address = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control rounded-2',
                   }
        ))
    # ramp_on_site = forms.BooleanField(
    #     widget=forms.CheckboxInput(
    #         attrs={
    #             'class': 'form-control'
    #         }
    #     ))
