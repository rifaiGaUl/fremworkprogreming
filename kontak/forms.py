from django import forms
from . models import Kontak

class KontakForm(forms.ModelForm):
    class Meta:
        model = Kontak
        fields = [ 'name', 'email', 'message']
