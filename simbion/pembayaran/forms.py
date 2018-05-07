from django import forms

text_input_attrs = {
    'type': 'text',
    'class': 'form-textinput',
}

number_input_attrs = {
    'type': 'number',
    'class': 'form-numberinput',
}

select_attrs = {'class': 'form-select'}

select_date_attrs = {'class': 'form-select-date'}


class PembayaranForm(forms.Form):
    urutan = forms.IntegerField(label='Urutan', required=True, widget=forms.NumberInput(attrs=number_input_attrs))
    kode_skema = forms.ChoiceField(label='Kode Skema Beasiswa', required=True, widget=forms.Select(attrs=select_attrs), choices=[])
    urutan_skema = forms.ChoiceField(label='Nomor Urut Skema Beasiswa', required=True, widget=forms.Select(attrs=select_attrs), choices=[], disabled=True)
    npm = forms.CharField(label='NPM', required=True, max_length=10, widget=forms.TextInput(attrs=number_input_attrs))
    keterangan = forms.CharField(label='Keterangan', required=True, max_length=50, widget=forms.TextInput(attrs=text_input_attrs))
    tanggal_bayar = forms.DateField(label='Tanggal Bayar', required=True, widget=forms.SelectDateWidget(attrs=select_date_attrs))
    nominal = forms.IntegerField(label='Nominal', required=True, widget=forms.NumberInput(attrs=number_input_attrs))
