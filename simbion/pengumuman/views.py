from django.shortcuts import render

response = {}
pengumuman = [
    {"tanggal": "20-02-2017", "judul": "Beasiswa Makan Kerupuk", "pembuat": "asereje"},
    {"tanggal": "17-04-2017", "judul": "Beasiswa Makan Teman", "pembuat": "DRE"},
    {"tanggal": "02-06-2017", "judul": "Beasiswa Citra Lestari", "pembuat": "ShanyITB"},
    {"tanggal": "20-06-2017", "judul": "Beasiswa Tupperware", "pembuat": "Alfamart"},
]

context = [
    {"kode": 14045, "urut": 2, "isi": "Far far away, behind the word mountains, far from the countries Vokalia and Consonantia, there live the blind texts. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean. A small river named Duden flows by"},
    {"kode": 1500600, "urut": 1, "isi": "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia vo"},
    {"kode": 12040, "urut": 8, "isi": "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium."},
    {"kode": 1500366, "urut": 2, "isi": "Li Europan lingues es membres del sam familie. Lor separat existentie es un myth. Por scientie, musica, sport etc, litot Europa usa li sam vocabular. Li lingues differe solmen in li grammatica, li pronunciation e li plu commun vocabules. Omnicos dire"},
]


def index(request):
    response['author'] = 'Benny William Pardede'
    response['pengumuman'] = pengumuman
    html = 'pengumuman/pengumuman.html'
    return render(request, html, response)


def content(request, index):
    response['author'] = 'Benny William Pardede'
    response['judul'] = pengumuman[index]['judul'].upper()
    response['kode'] = context[index]['kode']
    response['urut'] = context[index]['urut']
    response['pembuat'] = pengumuman[index]['pembuat']
    response['tanggal'] = pengumuman[index]['tanggal']
    response['isi'] = context[index]['isi']
    html = 'pengumuman/content.html'
    return render(request, html, response)
