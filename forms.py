from django import forms
from djangomodels.models import Toshiba

class wanafunziform(forms.ModelForm):
    class Meta:
        model=Toshiba
        fields="__all__"
            