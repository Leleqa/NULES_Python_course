from django import forms
from .models import Renters


class RentersForm(forms.ModelForm):
    class Meta:
        model = Renters
        fields = ['id', 'FirmName', 'Owner', 'PhoneNum']