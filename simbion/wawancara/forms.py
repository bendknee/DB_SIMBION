from django import forms


class WawancaraForm(forms.Form):
    error_messages = {'required': 'Tolong isi input ini.'}
    attrs = {
        'class': 'form-textinput',
        'cols': 50,
        'rows': 4
    }
    kode = forms.IntegerField(label='Kode', required=True, widget=forms.NumberInput(attrs=attrs))
    nama = forms.CharField(label='Nama', required=True, max_length=50, widget=forms.TextInput(attrs=attrs))
    lokasi = forms.CharField(label='Lokasi', required=True, max_length=50, widget=forms.TextInput(attrs=attrs))
