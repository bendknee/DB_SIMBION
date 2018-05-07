from django.shortcuts import render

mock_beasiswa1 = {"nama" : "Bank of Tokyo", "tanggal_tutup" : "31/05/2018", "status" : "Dibuka", "jumlah_pendaftar" : 50}
mock_beasiswa2 = {"nama" : "BEASISWA KADER SURAU YBM BRI TAHUN 2018", "tanggal_tutup" : "30/04/2018", "status" : "Ditutup", "jumlah_pendaftar" : 24}
response = {}

def index(request):
	beasiswa_list = [mock_beasiswa1, mock_beasiswa2]
	for i in range(len(beasiswa_list)):
		beasiswa_list[i]["no"] = i + 1
	response["beasiswa_list"] = beasiswa_list

	html = "lihat_beasiswa/lihat_beasiswa.html"
	return render(request, html, response)