--- START TUGAS 2 ---

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawaban:
Untuk memulai proyek Django baru, ikuti langkah-langkah berikut:
1. Buat virtual environment dengan perintah python -m venv env.
2. Aktifkan virtual environment dengan perintah env\Scripts\activate.
3. Buat file requirements.txt untuk daftar dependensi proyek Anda.
4. Jalankan perintah pip install -r requirements.txt untuk menginstal dependensi yang diperlukan.
5. Mulai proyek Django dengan perintah django-admin startproject proyek_pbp.
6. Untuk pengaturan deployment, tambahkan "*" pada ALLOWED_HOSTS di dalam settings.py.
7. Pastikan untuk menambahkan file .gitignore untuk menentukan berkas-berkas dan direktori-direktori yang tidak perlu disertakan dalam repositori Git.
8. Buat aplikasi dengan perintah python manage.py startapp main.
9. Di dalam direktori main, buat folder templates dan tambahkan file main.html sebagai tampilan aplikasi.
10. Lakukan routing untuk aplikasi main dengan menambahkan path('main/', include('main.urls')) pada urls.py di dalam proyek library_col.
11. Buat model Item di dalam aplikasi main dengan atribut wajib: name (CharField), amount (IntegerField), dan description (TextField).
12. Tambahkan fungsi show_main pada views.py yang akan merender template HTML dengan konteks nama aplikasi, nama, dan kelas Anda.
13. Lakukan deployment ke Adaptable untuk memungkinkan teman-teman Anda mengaksesnya melalui Internet.
14. Lakukan add, commit, dan push dari direktori repositori lokal ke GitHub.
15. Ikuti petunjuk Tutorial 0 untuk melakukan deploy dari website Adaptable.
Semua langkah di atas akan membantu Anda memulai proyek Django baru dan melakukan deployment ke Adaptable.

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Jawaban:

![Alt text](foto/image.png)

Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jawaban:
Virtual environment adalah komponen kunci dalam pengembangan aplikasi web Django karena memberikan isolasi proyek yang memungkinkan pengelolaan dependensi secara efisien. Dengan menggunakan virtual environment, setiap proyek dapat memiliki lingkungan Python dan dependensi tersendiri yang terisolasi, menghindari potensi konflik dan masalah versi. Ini juga menyederhanakan tata kelola dependensi proyek.
Selain manfaat tersebut, penggunaan virtual environment juga meningkatkan keamanan proyek dengan mencegah potensi konflik antara paket-paket yang digunakan dalam proyek berbeda. Secara keseluruhan, penggunaan virtual environment adalah praktik terbaik dalam pengembangan aplikasi Django karena memastikan kebersihan, isolasi, dan manajemen dependensi yang efisien.

Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
Jawaban:
Model-View-Controller (MVC), Model-View-Template (MVT), dan Model-View-ViewModel (MVVM) adalah pola desain arsitektur yang digunakan dalam pengembangan perangkat lunak.
MVC membagi aplikasi menjadi tiga komponen utama: Model (penyimpanan data dan logika aplikasi), View (menampilkan data dari Model dan menghubungkannya dengan template), dan Controller (mengontrol tampilan antarmuka pengguna).
MVT, sejenis dengan MVC, memisahkan aplikasi menjadi Model (menyimpan data dan logika), View (menampilkan data dari Model dan menghubungkannya dengan template), dan Template (mengelola tampilan HTML dan cara data dari Model ditampilkan dalam halaman web).
MVVM juga memisahkan aplikasi menjadi Model (menyimpan data dan logika), View (menampilkan data dari Model dan menghubungkannya dengan template), dan memperkenalkan ViewModel. ViewModel bertanggung jawab untuk memproses data dari Model dan mempersiapkannya agar dapat ditampilkan oleh View. Hal ini memungkinkan pengikatan data yang kuat antara Model dan View.
Perbedaan utama antara ketiganya terletak pada bagaimana mereka mengelola alur dan logika aplikasi. MVC memiliki Controller yang mengontrol alur aplikasi, MVT menggantinya dengan Template untuk mengelola tampilan, dan MVVM memperkenalkan ViewModel sebagai perantara antara Model dan View.

--- END TUGAS 2 ---



--- START TUGAS 3 ---

Apa perbedaan antara form POST dan form GET dalam Django?

Metode POST dan GET adalah dua cara berbeda untuk mengirimkan data ke target action. Metode POST mengirim data secara langsung tanpa memunculkannya di URL, menggunakan variabel $_POST untuk menampung nilai yang dikirim. Metode ini memungkinkan pengiriman data berukuran besar. Sementara itu, metode GET menampilkan data di URL, yang akan ditangani oleh action, dan memanfaatkan variabel $_GET untuk menampung nilai yang terdapat dalam URL. Metode GET memiliki batasan panjang URL sekitar 2047 karakter yang tidak boleh melebihi jumlah tersebut.

Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

XML (eXtensible Markup Language), JSON (JavaScript Object Notation), dan HTML (HyperText Markup Language) adalah tiga format yang berbeda dalam konteks pengiriman data. XML menggunakan tag pembuka dan penutup untuk mengorganisir data dalam hierarki yang kuat dan kompleks, sehingga cocok digunakan untuk pertukaran data antar sistem yang berbeda, konfigurasi file, dan dokumen dengan struktur yang lebih rumit. Di sisi lain, JSON adalah format data yang lebih sederhana, menggunakan sintaksis key-value. Ini biasanya digunakan untuk pertukaran data antar aplikasi web dan bahasa pemrograman yang berbeda, dan sering digunakan dalam pengembangan web untuk mengirim data antar server dan browser. HTML adalah bahasa markup yang berfokus pada pembuatan halaman web dengan menggambarkan tampilan dan struktur konten web, dan meskipun tidak digunakan secara langsung untuk pertukaran data, data dapat dimasukkan ke dalam atribut HTML atau dikelola oleh JavaScript pada halaman web. Dengan perbedaan struktur dan tujuan penggunaannya, ketiga format ini memiliki peran yang berbeda dalam lingkungan komputasi dan web modern.

Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

JSON memiliki keunggulan dalam beberapa aspek yang membuatnya menjadi pilihan utama dalam pertukaran data di lingkungan web. Pertama, dari segi kelegibilitas, JSON sangat mudah dipahami oleh manusia, memudahkan dalam membaca dan menginterpretasi data. Selain itu, dalam hal efisiensi, format JSON lebih ringkas dan hemat bandwidth dibandingkan dengan format lain. Kelebihan lainnya adalah dukungan universal, karena hampir semua bahasa pemrograman mendukung JSON. Hal ini membuatnya menjadi pilihan yang sangat fleksibel dalam pengembangan perangkat lunak. 
Selain itu, JSON juga memiliki keuntungan dalam integrasi dengan JavaScript, yang merupakan bahasa pemrograman yang sangat umum digunakan dalam pengembangan web. Format ini secara alami terintegrasi dengan JavaScript, mempermudah penggunaannya dalam proyek pengembangan web. Selain itu, JSON juga sangat umum digunakan dalam API web modern, menjadi standar de facto dalam pertukaran data antara server dan aplikasi klien. Lebih lanjut, JSON mendukung representasi objek, sesuai dengan pendekatan berbasis objek yang umum digunakan dalam pengembangan web. 
Dari segi keamanan, JSON juga memiliki keunggulan. Format ini jarang menghadapi masalah keamanan seperti serangan injeksi XML atau HTML, sehingga memberikan lapisan perlindungan tambahan terhadap ancaman keamanan potensial. Dengan berbagai keunggulan ini, tidak mengherankan bahwa JSON telah menjadi format yang dominan dan sangat diandalkan dalam pertukaran data di lingkungan web modern.

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Membuat Formulir Input Objek Model:
Buat file forms.py dalam folder "main" untuk membuat class ItemForm, yang akan digunakan sebagai ModelForm untuk model Item. Ini akan mendefinisikan atribut-atribut yang akan ditampilkan dalam formulir.

2. Membuat Fungsi untuk Input Data:
Di dalam views.py, buat fungsi create_item yang akan mengelola input data dari formulir. Fungsi ini akan mengisi formulir ItemForm dengan data dari request.POST dan akan memverifikasinya. Jika data valid, maka data tersebut akan disimpan dan pengguna akan diarahkan kembali ke halaman utama.

3. Membuat Fungsi untuk Merender Halaman Formulir:
Tambahkan fungsi untuk merender halaman create_item.html, yang akan digunakan untuk menampilkan formulir input data.

4. Mengambil Data dari Database:
Di dalam fungsi show_main dalam views.py, tambahkan perintah items = Item.objects.all() untuk mengambil semua objek Item dari database dan menyertakannya dalam konteks.

5. Mengatur URL:
Impor fungsi yang diperlukan dan tambahkan path URL dalam file urls.py di "main" untuk mengakses fungsi-fungsi ini.

6. Membuat Halaman HTML untuk Formulir:
Buat file create_item.html dalam folder "templates" di "main" dan isi dengan kode HTML yang sesuai untuk membuat antarmuka tabel dan formulir input data.

7. Menampilkan Data dalam Halaman Utama:
Tambahkan kode di dalam file main.html untuk menampilkan data item dalam bentuk tabel dan tambahkan tombol "Add New Product" yang mengarahkan ke halaman formulir input data.

8. Menambahkan Fungsi Views untuk Melihat Data dalam Berbagai Format:
- Buat fungsi show_xml dalam views.py dan tambahkan path URL untuk mengaksesnya. Fungsi ini akan mengambil data Item dan mengembalikkannya dalam format XML.
- Buat fungsi show_json dalam views.py dan tambahkan path URL untuk mengaksesnya. Fungsi ini akan mengambil data Item dan mengembalikkannya dalam format JSON.
- Buat fungsi show_xml_by_id dalam views.py dan tambahkan path URL untuk mengaksesnya. Fungsi ini akan mengambil data Item berdasarkan ID yang disediakan dan mengembalikkannya dalam format XML.
- Buat fungsi show_json_by_id dalam views.py dan tambahkan path URL untuk mengaksesnya. Fungsi ini akan mengambil data Item berdasarkan ID yang disediakan dan mengembalikkannya dalam format JSON.

Screenshot POSTMAN:
1. HTML
![Alt text](foto/image-1.png)
![Alt text](foto/image-2.png)

2. XML
![Alt text](foto/image-3.png)

3. JSON
![Alt text](foto/image-4.png)

4. XML by ID
![Alt text](foto/image-6.png)

5. JSON by ID
![Alt text](foto/image-5.png)

--- END TUGAS 3 ---