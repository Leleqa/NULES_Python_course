from django import forms
from .models import Todo
from .models import Renters


class TodoForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'completed']

class RentersForm(forms.ModelForm):
    class Meta:
        model = Renters
        fields = ['id', 'FirmName', 'Owner', 'PhoneNum']