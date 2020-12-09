from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import UserProfile
from core.BootstrapFormMixin import BootstrapFormMixin


class SignUpForm(UserCreationForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_up_form()


class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = UserProfile
        fields = '__all__'

