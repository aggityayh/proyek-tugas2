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

Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

UserCreationForm pada Django adalah modul bawaan atau importan yang memfasilitasi formulir pendaftaran pengguna. Modul ini digunakan untuk menghemat waktu dan memastikan validasi data pengguna. Dengan UserCreationForm, kita dapat fokus pada pengembangan fitur khusus aplikasi, tanpa perlu menulis kode pembuatan formulir dari awal. Formulir ini mencakup username, password, dan konfirmasi password. Kelebihannya juga termasuk kemampuan untuk menyesuaikan formulir dengan tambahan menu yang kita diperlukan. UserCreationForm menyimpan data pengguna dengan aman di database sesuai standar keamanan Django. Dengan demikian, UserCreationForm adalah alat yang sangat berguna untuk mengoptimalkan proses pendaftaran pengguna di situs web Django.


Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

Autentikasi berkaitan dengan proses verifikasi identitas pengguna atau user. Autentikasi memastikan bahwa yang mengisi input data diri adalah mereka yangn memang sudah pernah mendaftarkan diri mereka. Django menyediakan sistem autentikasi bawaan yang memungkinkan pengguna mendaftar, masuk, dan mengelola akun mereka secara personal.
Otorisasi berkaitan dengan hak akses pengguna setelah mereka terautentikasi. Otorisasi menentukan apa yang dapat atau tidak dapat dilakukan pengguna di dalam aplikasi berdasarkan peran atau izin yang mereka miliki. Django memiliki sistem otorisasi yang kuat yang memungkinkan pengembang mengontrol akses ke bagian-bagian tertentu dari aplikasi.
Kedua hal diatas penting karena mereka bekerja sama untuk menjaga keamanan dan privasi pengguna aplikasi. Autentikasi memastikan bahwa hanya pengguna yang sah yang dapat mengakses akun mereka, sementara otorisasi memastikan bahwa setiap pengguna memiliki hak akses yang sesuai dengan perannya. Dengan cara ini, Django membantu pengembang untuk membangun aplikasi yang aman dan terstruktur dengan baik.


Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?


Cookies dalam konteks aplikasi web adalah file teks kecil yang disimpan di perangkat pengguna saat mereka berinteraksi dengan situs web dan akan diambil kembali nantinya saat data file tersebut dibutuhkan. Cookies membuat aplikasi mengingat preferensi, personalisasi, dan/atau status pengguna selama mengakses aplikasi web. 
Django menggunakan cookies untuk mengelola data dari setiap sesi pengaksesan web oleh pengguna. Ketika pengguna pertama kali mengunjungi situs web, Django akan membuat cookie unik untuk pengguna tersebut. Cookie akan mengidentifikasi aktivitas pengguna dan memproses data yang dianggap unik ke server. Informasi seperti status login atau preferensi, akan disimpan secara aman di server.
Setiap kali pengguna melakukan permintaan ke situs aplikasi web, data cookies akan dikirimkan ke server untuk mengidentifikasi aktivitas pengguna tersebut dan memberikan pengalaman yang lebih baik ke pengguna.


Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

Secara default, penggunaan cookies dalam pengembangan web memiliki beberapa lapisan keamanan, terutama jika digunakan dengan HTTPS. Namun, keamanannya juga sangat tergantung pada bagaimana cookies diimplementasikan dalam aplikasi. Namun berdasarkan informasi yang saya dapat, terdapat beberapa potensi resiko yang patut diwaspadai antara lain:
1. Risiko Pencurian Data karena cookies dapat menjadi target potensial bagi penyerang yang mencoba mencuri informasi sensitif seperti token otentikasi atau informasi pribadi pengguna.
2. Cross-Site Scripting (XSS), dimana terjadi jika aplikasi tidak mengimplementasikan langkah-langkah perlindungan yang memadai, sehingga cookies dapat menjadi rentan terhadap serangan XSS, dimana penyerang memasukkan skrip berbahaya yang dapat mencuri atau memanipulasi cookie.
3. Cross-Site Request Forgery (CSRF) yang diakibatkan saat cookies yang tidak diatur dengan benar sehingga menyebabkan kerentanan CSRF, serangan dapat memaksa pengguna untuk melakukan tindakan yang tidak diinginkan tanpa sepengetahuan mereka.
4. Session Hijacking atau Sidejacking hal ini terjadi jika koneksi tidak dienkripsi dengan baik, serangan dapat memantau atau mencuri cookie saat berkomunikasi dengan server, yang dapat memungkinkan akses ilegal ke sesi pengguna.
5. Cookie Mismatch apabila pengaturan cookie yang tidak tepat akan dapat menyebabkan masalah dengan integritas sesi pengguna, memungkinkan serangan manipulasi sesi.
6. Kebocoran Informasi dimana jika cookie mengandung informasi sensitif tanpa enkripsi atau tindakan keamanan tambahan, informasi tersebut dapat bocor jika cookie dicuri atau digunakan oleh pihak yang tidak berwenang.


Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Registrasi, Login, dan Logout:
Untuk memungkinkan pengguna mengakses aplikasi dengan lancar, pertama-tama kita harus mengimplementasikan fungsi registrasi, login, dan logout. Dalam file views.py, kita akan mengimpor modul yang diperlukan seperti redirect, UserCreationForm, messages, authenticate, dan login. Selanjutnya, kita akan membuat fungsi register yang akan menghasilkan formulir registrasi secara otomatis dan membuat akun pengguna saat data dikirimkan melalui formulir. Kita juga perlu membuat file HTML baru bernama register.html di dalam folder main/templates untuk membuat tampilan formulir registrasi. Fungsi login akan mengautentikasi pengguna yang ingin masuk ke aplikasi. Kita juga akan membuat file HTML baru bernama login.html di dalam folder main/templates untuk tampilan halaman login. Terakhir, kita akan menambahkan fungsi logout yang akan mengatur mekanisme logout. Ini akan melibatkan menghapus sesi pengguna. Semua fungsi ini akan diimpor ke dalam urls.py, dan kita akan menambahkan path URL ke dalam urlpatterns.
2. Membuat Akun Pengguna dengan Data Dummy:
Langkah selanjutnya adalah membuat dua akun pengguna dan masing-masing akun akan memiliki tiga data dummy. Tahap ini akan melibatkan penggunaan model yang telah kita buat sebelumnya dalam aplikasi. Data dummy ini akan digunakan untuk menguji fungsionalitas aplikasi.
![Alt text](foto/dummy1.png)
![Alt text](foto/dummy2.png)
3. Menghubungkan Model Item dengan User:
Untuk menghubungkan model Item dengan User, kita akan memodifikasi model Item dengan menambahkan ForeignKey yang akan menciptakan hubungan antara satu produk dan satu pengguna. Dalam views.py, kita juga akan mengubah fungsi create_item dengan menambahkan parameter commit=False untuk mencegah data disimpan langsung ke database. Kemudian, kita akan mengisi bidang user dengan objek User dari request.user untuk menandakan bahwa produk tersebut dimiliki oleh pengguna yang sedang login.
4. Menampilkan Informasi Pengguna yang Sedang Login:
Untuk menampilkan detail informasi pengguna yang sedang login seperti nama pengguna (username) dan menerapkan cookies seperti waktu terakhir login pada halaman utama aplikasi, kita akan mengubah fungsi show_main. Kita akan menggunakan Item.objects.filter(user=request.user) untuk menampilkan produk yang terkait dengan pengguna yang sedang login. Selain itu, kita akan menambahkan kode untuk menampilkan waktu terakhir login dengan request.COOKIES['last_login']. Untuk mengatur cookie waktu terakhir login, kita akan mengubah fungsi login_user, dan pada saat logout, kita akan menghapus cookie ini. Kemudian, pada tampilan halaman utama (main.html), kita akan menampilkan waktu terakhir login dengan elemen HTML <h5>Sesi terakhir login: {{ last_login }}</h5>

--- START TUGAS 3 ---