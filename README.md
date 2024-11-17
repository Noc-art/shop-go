**Pacil Web Service**: http://nevin-thang-shopgo.pbp.cs.ui.ac.id/

**TUGAS 2**

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Inisialisasi: Langkah pertama yang dilakukan adalah membuat repositori Git untuk proyek ini, baik secara lokal maupun di Github. Setelah itu, saya menyiapkan lingkungan untuk mengembangkan proyek dengan membuat virtual environment untuk mengisolasi depedensi dan memastikan kompatibilitas versi. Kita harus memastikan untuk mengaktivasi virtual environment sebagai langkah dasar dalam mengembangkan proyek Django ini.
- Struktur proyek: Kita membuat struktur proyek yang terorganisir agar pengembangan lebih efisien dan mudah untuk dipelihara. Selanjutnya, kita dapat menginstal depedensi yang diperlukan melalui requirements.txt seperti Django. Lalu, buat file .gitignore untuk mengecualikan file yang tidak relevan agar tidak dipush pada version control.
- Pembuatan aplikasi: Kita membuat aplikasi utama dalam proyek Django untuk e-commerce. Selain itu, kita membuat folder templates untuk menyimpan file HTML yang akan menampilkan user interface. Lalu, kita membangun model sesuai kebutuhan aplikasi, dalam konteks e-commerce kita membuat model Product untuk menyimpan informais produk.
- Konfigurasi URL routing: Kita mengatur routing URL pada konfigurasi urls.py pada lingkup proyek maupun aplikasi agar setiap request dapat diarahkan ke view yang tepat. Kita juga menulis unit test untuk setiap view dan model untuk memastikan kode berjalan lancar dan meminimalkan potensi keberadaan bug.
- Dokumentasi : Kita membuat file README.md di root repositori untuk mendokumentasikan detail proyek.
- Version control : Kita menggunakan kontrol versi dengan Git untuk melacak perubahan kode dan mendukung penggunaan branching dan merging. Setelah proyek siap, push proyek ke repositori GitHub untuk mencadangkan kode, memungkinkan akses dari mana saja, dan kolaborasi dengan pengembang lainnya.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
   Link: https://www.canva.com/design/DAGQXkEZIc4/3FbaZbPt4E-5tWRO6UXNUQ/edit?utm_content=DAGQXkEZIc4&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
   ![Bagan Request Client](https://github.com/user-attachments/assets/7e6a88af-e0e3-4367-aa1d-ebe33b72a25c)


4. Jelaskan fungsi git dalam pengembangan perangkat lunak!
   Git adalah sebuah sistem version control. Git dapat digunakan untuk melacak perubahan kode secara terperinci dan memungkinkan pengembang untuk mengembalikan ke versi sebelumnya. Dengan berbagai fiturnya seperti Branching dan Merging, Git mendukung kolaborasi antar pengembang untuk bekerja pada kode yang sama dengan mengelola cabang yang berbeda dan mengatasi konflik saat penggabungan kode. Git juga memungkinkan pengembang untuk melakukan back-up dan mencegah kehilangan data. Saat ini, Git sangat banyak digunakan pada dunia pengembangan perangkat lunak.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
   Selain popularitas dan penggunaan Django di dunia industri, Django mendukung pembelajaran yang terstruktur melalui implementasi konsep Model-View-Template (MVT). Hal ini mempermudah pelajar dalam memahami best practice dalam pengembangan. Django juga memiliki dokumentasi yang sangat lengkap dan memiliki komunitas pengguna yang aktif sehingga mendukung pembelajaran. Yang terakhir, fitur keamanan built-in Django juga turut membantu pembelajar dalam mencegah berbagai ancaman yang ada.

6. Mengapa model pada Django disebut sebagai ORM?
   ORM atau yang memiliki kepanjangan (Object-Relational Mapping) adalah sebuah teknik pemrograman yang digunakan untuk menghubungkan antara objek-objek dalam kode program berorientasi objek dengan tabel-tabel dalam basis data relasional. Model pada Django disebut sebagai ORM karena dia bertindak sebagai jembatan antara kode program yang ditulis dalam bahasa Object Oriented Programming seperti Python dan basis data relasional seperti SQLite, PostgreSQL, atau MySQL yang digunakan oleh aplikasi.

**TUGAS 3**

1. Mengapa Kita Memerlukan Data Delivery dalam Pengimplementasian Sebuah Platform?
Data delivery adalah proses mengirimkan data dari satu sistem ke sistem lain atau dari backend ke frontend dalam sebuah platform. Proses ini memastikan bahwa semua bagian dari platform memiliki data yang konsisten dan membantu mengintegrasikan berbagai layanan dan sistem dengan memastikan bahwa data dapat dikirim dan diterima dengan benar antara sistem yang berbeda. Selain itu, pengiriman data memastikan bahwa data yang dikirimkan aman dan tidak terjadi kesalahan saat dikirimkan.

2. Mana yang Lebih Baik antara XML dan JSON? Mengapa JSON Lebih Populer Dibandingkan XML?
JSON lebih populer dibandingkan XML karena lebih sederhana dan mudah dibaca. Hal ini disebabkan oleh format JSON yang tidak memerlukan tag pembuka dan penutup seperti XML. Parsing JSON juga biasanya lebih cepat dan efisien karena struktur datanya yang lebih sederhana. Selain itu, JSON termasuk dalam ekosistem JavaScript, yang merupakan bahasa yang paling populer dalam pengembangan web.  Banyaknya API modern yang telah menggunakan JSON dikarenakan kecepatan pengiriman dan ukuran data yang lebih kecil, juga turut membuat penggunaan JSON lebih mendominasi. 

3. Fungsi dari Method is_valid() pada Form Django dan Mengapa Kita Membutuhkan Method Tersebut?
is_valid() adalah method dalam Django yang digunakan untuk memvalidasi data yang diinput ke dalam form. Method ini memastikan bahwa data yang dimasukkan ke dalam form sesuai dengan aturan validasi yang telah didefinisikan, seperti tipe data dan lain-lain.Jika data tidak valid, is_valid() akan mengembalikan False dan memberikan pesan kesalahan, sehingga pengguna bisa memperbaiki kesalahan input mereka. Hal ini membuat potensi bug menjadi lebih kecil.

4. Mengapa Kita Membutuhkan csrf_token Saat Membuat Form di Django? Apa yang Dapat Terjadi Jika Kita Tidak Menambahkan csrf_token pada Form Django? Bagaimana Hal Tersebut Dapat Dimanfaatkan oleh Penyerang?
csrf_token (Cross-Site Request Forgery Token) adalah token unik yang digunakan untuk mencegah serangan CSRF. Ini memastikan bahwa permintaan (request) yang dibuat oleh pengguna sah berasal dari situs yang benar. Token ini membuat setiap permintaan POST unik dan diverifikasi oleh server, sehingga mengurangi risiko serangan. Jika kita tidak menambahkan csrf_token, penyerang bisa dengan mudah melakukan serangan CSRF dengan mengirimkan permintaan berbahaya atas nama pengguna yang terautentikasi. Penyerang bisa membuat situs atau skrip yang mengirimkan permintaan POST ke server target. Jika csrf_token tidak ada atau tidak diperiksa, server akan memproses permintaan tersebut seolah-olah itu sah.

5. Bagaimana Cara Mengimplementasikan Checklist di Atas Secara Step-by-Step?
- Membuat skeleton: Saya melakukan perubahan pada folder templates dan membangun skeleton sebagai kerangka untuk views dari website saya. Hal ini dilakukan untuk menciptakan lingkungan yang lebih terstruktur dan mencegah redudansi
- Mengubah Primary key menjadi UUID: Saya mengubah primary key menjadi UUID guna meningkatkan keamanan pada website dan melakukan migrasi model
- Pembuatan Form: Saya membuat forms.py yang berisi form untuk entry produk yang sederhana. Lalu, saya melakukan perubahan pada views.py untuk menambahkan form. Pada urls.py, saya juga mengatur konfigurasi dengan menambahkan path baru ke views yang baru saya buat. Agar tampil pada website, saya juga menambahkan form tersebut pada file html.
- Mengembalikan data dalam XML dan JSON:  Saya menambahkan fungsi baru untuk mengembalikan data XML dan JSON serta pengembaliannya berdasarkan ID. Lalu, saya kembali mengkonfigurasikan urls.py dengan menambahkan path
- Postman: melakukan pengecekan XML dan JSON pada data viewer untuk memastikan keberhasilkan kode.
- Dokumentasi: Membuat README.md untuk mendokumentasikan kode yang telah dibuat
- Version Control: Melakukan push ke GitHub untuk menyimpan versi terbaru kode shop-go.

POSTMAN XML
![image](https://github.com/user-attachments/assets/cd9fbe57-c3b8-4c02-be81-fbdc4d0dc805)

POSTMAN XML by ID
![image](https://github.com/user-attachments/assets/fefac668-0465-46a3-bf1c-21e1cdbadddd)

POSTMAN JSON
![image](https://github.com/user-attachments/assets/b8d2b6ff-508a-4a53-896f-67d3ae2188dc)

POSTMAN JSON by ID
![image](https://github.com/user-attachments/assets/3f6ef26a-0afb-4779-95b4-79bac0ded13c)


**Tugas 4**
1. Perbedaan antara HttpResponseRedirect() dan redirect() di Django:
HttpResponseRedirect() memerlukan URL yang akan dijadikan tujuan redirect sebagai argumen, sedangkan redirect() merupakan shortcut function di Django yang lebih sederhana dibandingkan HttpResponseRedirect(). Kita dapat memberikan URL, nama view, atau bahkan objek model sebagai argumen, dan Django akan mengurus konversi ini menjadi URL yang valid. redirect() lebih mudah digunakan dan disarankan untuk digunakan jika tidak ada kebutuhan khusus.

2. Cara Kerja Penghubungan Model Product dengan User
Dalam menghubungkan model Product dengan User, kita menggunakan relationship One to Many dimana setiap pengguna dapat memiliki beberapa produk. Pertama-tama kita membuat terlebih dahulu model product yang bereferensi ke model user.

```
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
```

Untuk mengakses data produk yang dimiliki pengguna tertentu, kita dapat menggunakan query untuk mendapatkan produk sesuai dengan pemiliknya.
```
product_entries = Product.objects.filter(user=request.user)
```

3.  Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
- Authentication adalah proses verifikasi identitas pengguna, yang bertujuan menjawab pertanyaan “siapa” yang akan login dengan melakukan validasi. Dalam Django, ini melibatkan pemeriksaan username dan password. Ketika pengguna login, Django memeriksa kredensial tersebut dan jika valid, pengguna akan terotentikasi.
- Authorization adalah proses mengevaluasi apakah pengguna yang sudah terotentikasi memiliki izin atau hak akses untuk melakukan tindakan tertentu. Setelah login, Django memeriksa hak akses pengguna untuk menentukan tindakan apa saja yang diizinkan untuk dilakukan. Ini dilakukan untuk mencegah pengguna yang tidak sah melakukan tindakan yang tidak diizinkan.
- Saat pengguna login, pertama-tama pengguna akan mengisi form login menggunakan username dan password yang telah dibuat sebelumnya. Lalu, Django akan melakukan autentikasi memverifikasi identitas pengguna. Lalu, sesi akan diciptakan untuk para pengguna. 
- Django dapat mengimplementasikan authentication menggunakan django.contrib.auth yang menyediakan view dan form untuk login, logout, dan registrasi. Saat pengguna login, Django akan memeriksa apakah kredensial benar dan, jika benar, akan membuat sesi untuk pengguna dan authorization menggunakan decorators seperti @login_required untuk membatasi akses ke view tertentu. Dengan ini, hanya pengguna yang telah terautentikasi yang bisa mengakses view tersebut. 

5. Bagaimana Django Mengingat Pengguna yang Telah Login
Django mengingat pengguna yang telah login dengan menggunakan session dan cookie. Session adalah cara untuk menyimpan informasi di server tentang pengguna yang sedang aktif. Setiap pengguna yang mengakses aplikasi akan mendapatkan sesi unik yang diidentifikasi melalui ID sesi. Cookie adalah data kecil yang disimpan di sisi klien (browser) untuk menyimpan informasi yang dapat diakses oleh server. Cookie juga memiliki banyak kegunaan lain seperti menyimpan preferensi pengguna, pelacakan aktivitas, dan aktivitas lainnya seperti menyimpan item di keranjang belanja e-commerce. Sayangnya, tidak semua cookie aman karena rentan terhadap serangan XSS dan CSRF. Hal ini dapat dicegah dengan menggunakan atribut keamanan cookie seperti  HttpOnly, Secure, SameSite.

6. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- Membuat fungsi register, login, dan logout pada views.py menggunakan library django.contrib.auth
- Menambahkan path dari fungsi tersebut ke urls.py
- Melakukan restriksi akses ke halaman show_main dengan mengatur authorization dengan decorator @login_required
- Memanfaatkan cookies untuk membuat output last_login
- Membuat template HTML untuk registrasi, login, dan logout
- Membuat dummy user
- Menghubungkan product dan user dengan mereferensikan model product ke user dan memfilter product sesuai user yang sedang login.
- Migrate model yang telah diperbaharui
- Melakukan dokumentasi menggunakan README.md

Contoh user 1
![image](https://github.com/user-attachments/assets/b61fc1dc-5245-4f5f-ace0-df58e5a1d20b)

Contoh user 2
![image](https://github.com/user-attachments/assets/f3e45909-d6a0-4d99-bddb-33b26a14ab13)

**Tugas 5**
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut! 
Jika terdapat beberapa CSS selector untuk suatu elemen HTML, urutan prioritas pengambilan CSS selector akan ditentukan berdasarkan beberapa faktor:
- Jika kita memiliki beberapa CSS selector, maka akan terdapat urutan prioritas sebagai berikut:
- Inline styles memiliki prioritas tertinggi.
- ID selectors  lebih spesifik dan memiliki prioritas lebih tinggi dibanding class, atribut, dan type selectors.
- Class selectors, attribute selectors, dan pseudo-class selectors memiliki prioritas lebih rendah dari ID selectors, namun lebih tinggi dari type selectors.
- Type selectors dan pseudo-element selectors memiliki prioritas paling rendah.
- Jika dua selector memiliki specificity yang sama, yang terakhir diurutkan di CSS yang akan diterapkan.

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive Design adalah teknik atau metode yang digunakan oleh web designer untuk menciptakan layout website yang dapat menyesuaikan diri dengan ukuran layar pengguna. Dengan cara ini, pengalaman pengguna ditingkatkan karena situs menjadi lebih mudah diakses dan digunakan di berbagai perangkat. Contoh aplikasi yang telah menerapkan responsive design adalah Google, yang menggunakan tata letak responsif untuk menyesuaikan antarmuka di berbagai perangkat. Di sisi lain, aplikasi yang belum menerapkan responsive design dapat dilihat dalam situs web pemerintahan. 

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
- Margin adalah jarak luar antara elemen dan elemen lain di sekitarnya, berfungsi untuk memberi ruang kosong yang bikin tata letak jadi lebih rapi. 
'''
.element {
    margin: 20px; 
    margin-top: 10px; 
    margin-bottom: 15px; 
    margin-left: 5px; 
    margin-right: 5px; 
}
'''
- Border adalah garis yang mengelilingi elemen, memisahkan padding dari margin dan memberikan batas yang jelas. 
'''
.element {
    border: 2px solid black; 
    border-top: 3px dashed red; 
    border-radius: 5px; 
}
'''
- Padding adalah jarak di dalam elemen, antara konten dan tepi border, yang membuat konten tidak terlalu dekat dengan batas. 
'''
.element {
    padding: 15px; 
    padding-top: 10px; 
    padding-bottom: 5px; 
    padding-left: 20px; 
    padding-right: 20px; 
}
'''
Berikut contoh dari margin,border, dan padding
![images](https://github.com/user-attachments/assets/e867eff3-095f-45f5-b6c2-1acff3ebd0da)

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
- Flexbox  dirancang untuk layout satu dimensi, baik itu secara horizontal atau vertikal. Flexbox sangat berguna saat kamu ingin menyusun elemen dalam satu arah dan mengatur ruang antar elemen dengan lebih mudah. Kegunaannya termasuk memudahkan pembuatan layout responsif untuk elemen baris atau kolom yang fleksibel, seperti navbar atau galeri gambar.
- Grid Layout adalah sistem tata letak dua dimensi yang memungkinkan pengaturan elemen di baris dan kolom secara bersamaan. Grid sangat cocok untuk membuat layout yang lebih kompleks, karena dapat mengatur elemen secara horizontal dan vertikal sekaligus.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
- Implementasi Tailwind CSS: Pertama-tama, saya mengintegrasikan Tailwind CSS sebagai framework CSS pada aplikasi Django saya. Proses ini melibatkan penambahan Tailwind ke dalam pengaturan proyek serta pengaturan file konfigurasi yang diperlukan agar Tailwind dapat berfungsi dengan baik.
- Pengembangan Fitur Edit dan Hapus Produk: Saya menambahkan berbagai fitur pada aplikasi, termasuk fungsi untuk mengedit dan menghapus produk. Fitur ini memungkinkan pengguna untuk dengan mudah melakukan pembaruan atau penghapusan data produk, meningkatkan interaktivitas dan fleksibilitas aplikasi.
- Pembuatan Navbar: Saya merancang dan membuat komponen navbar dengan membuat file navbar.html di dalam direktori aplikasi. Navbar ini berfungsi sebagai elemen navigasi utama yang memungkinkan pengguna untuk berpindah antar halaman dengan mudah.
- Implementasi Navbar pada Template HTML: Setelah membuat navbar, saya mengimplementasikannya di berbagai template HTML lainnya dalam aplikasi. Hal ini memastikan konsistensi dalam navigasi di seluruh halaman aplikasi.
- Penambahan Static Files untuk CSS dan Gambar: Saya menambahkan file statis, termasuk CSS dan gambar, ke dalam aplikasi untuk mendukung tampilan dan nuansa aplikasi. Ini termasuk mengorganisir file statis dalam struktur direktori yang sesuai agar mudah diakses.
- Styling Menggunakan Tailwind CSS: Terakhir, saya menerapkan styling CSS menggunakan Tailwind yang telah ditambahkan sebelumnya. Dengan memanfaatkan utility classes dari Tailwind, saya dapat menciptakan desain yang responsif dan modern tanpa perlu menulis banyak kode CSS secara manual.

**Tugas 6**
1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
JavaScript memungkinkan kita untuk membuat suatu website yang responsif dan dinamis. Kita dapat menambahkan animasi, formulir validasi, dan konten dinamis tanpa perlu memuat ulang halaman. JavaScript juga dapat mengubah, menambah, atau menghapus elemen HTML di halaman secara dinamis. Dengan bantuan AJAX, JavaScript juga dapat melakukan Asynchronous Web Communication.

2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
await digunakan untuk menunggu hasil dari promise yang dikembalikan oleh fetch(). Dengan menggunakan await, eksekusi kode akan berhenti hingga promise tersebut diselesaikan atau ditolak. Jika tidak Menggunakan await, program akan langsung melanjutkan eksekusi tanpa menunggu data dari fetch(). Ini dapat menyebabkan kode mencoba mengakses data yang belum tersedia, yang dimana akan menghasilkan error.

3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
csrf_exempt digunakan untuk menonaktifkan pemeriksaan CSRF (Cross-Site Request Forgery) pada view yang akan digunakan untuk menerima request POST dari AJAX. Untuk pengembangan awal, menggunakan csrf_exempt dapat mengurangi kerumitan dan memungkinkan pengujian fungsionalitas tanpa gangguan. Kita menjadi tidak perlu menyertakan token CSRF dalam setiap permintaan AJAX.

4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Pembersihan data di backend sangat penting untuk mencegah serangan seperti SQL Injection dan XSS. Dengan pembersihan ini, data yang disimpan di server bisa dipastikan valid, terlepas dari apa yang dikirim oleh pengguna. Melakukan pembersihan di frontend dan backend adalah praktik terbaik untuk menjaga keamanan data.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
- Membuat Views dan Routing URL: saya menyiapkan view di Django untuk menangani request AJAX dan tambahkan routing URL yang sesuai.
- Mengimplementasikan API fetch(): saya menggunakan fetch() di JavaScript dengan async dan await untuk mengirim data produk ke server secara asinkron.
- Membuat Modal untuk Form Penambahan Produk: saya membuat modal di HTML yang berisi form untuk menginput data produk, seperti nama, harga, dan deskripsi.
- Membuat Fungsi untuk Menambahkan Produk: saya membuat fungsi JavaScript yang mengumpulkan data dari form dan memanggil fungsi addProduct() untuk mengirim data ke server.
- Mengimplementasikan Pencegahan XSS: saya menggunakan strip_tags di Django dan DOMPurify di frontend untuk menghapus tag HTML berbahaya dari input pengguna.
