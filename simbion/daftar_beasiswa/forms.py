from django import forms

JENIS_PAKET_BEASISWA = [("Beasiswa Prestasi Akademik", "Beasiswa Prestasi Akademik"),
						("Beasiswa Bantuan Belajar", "Beasiswa Bantuan Belajar"),
						("Beasiswa Tugas Akhir", "Beasiswa Tugas Akhir")]

error_messages = {'required': 'Tolong isi input ini.'}

text_input_attrs = {
	'type': 'text',
	'class': 'form-textinput',
}

text_area_attrs = {
	'type': 'text',
	'cols': 50,
	'rows': 4,
	'class': 'form-textarea',
	'placeholder':'Masukan deskripsi...'
}

select_attrs = {'class' : 'form-select'}

select_date_attrs = {'class' : 'form-select-date'}

class Daftar_Beasiswa_Form(forms.Form):
	kode = forms.CharField(label='Kode', label_suffix=' : ', required=True,
		widget=forms.TextInput(attrs=text_input_attrs))

	nama_paket_beasiswa = forms.CharField(label='Nama Paket Beasiswa', label_suffix=' : ',
		required=True, widget=forms.TextInput(attrs=text_input_attrs))

	jenis_paket_beasiswa = forms.ChoiceField(label='Jenis Paket Beasiswa', label_suffix=' : ',
		required=True, widget=forms.Select(attrs=select_attrs), choices=JENIS_PAKET_BEASISWA)

	deskripsi = forms.CharField(label='Deskripsi', label_suffix=' : ', required=True,
		widget=forms.Textarea(attrs=text_area_attrs))

	syarat_beasiswa = forms.CharField(label='Syarat Beasiswa', label_suffix=' : ', required=True,
		widget=forms.Textarea(attrs=text_area_attrs))

class Tambah_Beasiswa_Aktif_Form(forms.Form):
	kode_beasiswa = forms.ChoiceField(label='Kode Beasiswa', label_suffix=' : ',
		required=True, widget=forms.Select(attrs=select_attrs), choices=[]) # empty list for now

	nomor_urut = forms.CharField(label='Nomor Urut', label_suffix=' : ', required=True,
		widget=forms.TextInput(attrs=text_input_attrs))

	tanggal_mulai_pendaftaran = forms.DateField(label='Tanggal Mulai Pendaftaran', label_suffix=' : ', required=True,
		widget=forms.SelectDateWidget(attrs=select_date_attrs))

	tanggal_tutup_pendaftaran = forms.DateField(label='Tanggal Tutup Pendaftaran', label_suffix=' : ', required=True,
		widget=forms.SelectDateWidget(attrs=select_date_attrs))