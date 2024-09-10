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
