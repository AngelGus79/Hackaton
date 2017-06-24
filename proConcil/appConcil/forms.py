from .models import modelLey
from django import forms


class formLey(forms.ModelForm):
    class Meta:
        model = modelLey
        fields = "__all__"
        widgets = {
            'Ag': forms.TextInput(attrs={'class': 'form-control'}),
            'Av': forms.TextInput(attrs={'class': 'form-control'}),
            'Pd': forms.TextInput(attrs={'class': 'form-control'}),
            'Zn': forms.TextInput(attrs={'class': 'form-control'}),
            'Cu': forms.TextInput(attrs={'class': 'form-control'}),
        }
