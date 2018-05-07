from django.shortcuts import render

mock_beasiswa1 = {"kode" : 82390, "nama" : "Bank of Tokyo", "jenis" : "Beasiswa Bantuan Belajar", "tanggal_tutup" : "31/05/2018",
				"donatur" : "DON123" , "status" : "Dibuka", "jumlah_pendaftar" : 50,
				"deskripsi" : " Besaran yang didapatkan dari beasiswa ini adalah sebesar Rp6.000.000,-/mahasiswa setiap semester untuk pembayaran biaya pendidikan.",
				"syarat" : "IPK >= 3,25"}
mock_beasiswa2 = {"nama" : "BEASISWA KADER SURAU YBM BRI TAHUN 2018", "tanggal_tutup" : "30/04/2018", "status" : "Ditutup", "jumlah_pendaftar" : 24}

response = {}

def index(request):
	beasiswa_list = [mock_beasiswa1, mock_beasiswa2]
	for i in range(len(beasiswa_list)):
		beasiswa_list[i]["no"] = i + 1
	response["beasiswa_list"] = beasiswa_list

	html = "lihat_beasiswa/lihat_beasiswa.html"
	return render(request, html, response)

def detail_beasiswa(request):
	html = "lihat_beasiswa/detail_beasiswa.html"
	response["beasiswa"] = mock_beasiswa1
	return render(request, html, response)