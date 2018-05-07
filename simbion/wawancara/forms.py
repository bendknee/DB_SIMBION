from django import forms


class WawancaraForm(forms.Form):
    attrs = {
        'class': 'form-control'
    }
    kode = forms.IntegerField(label='Kode', required=True, widget=forms.NumberInput(attrs=attrs))
    nama = forms.CharField(label='Nama', required=True, max_length=50, widget=forms.TextInput(attrs=attrs))
    lokasi = forms.CharField(label='Lokasi', required=True, max_length=50, widget=forms.TextInput(attrs=attrs))
