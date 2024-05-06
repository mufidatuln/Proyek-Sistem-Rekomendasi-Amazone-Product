# Laporan Proyek Machine Learning - Mufidatul Ngazizah

## Project Overview
Dengan pertumbuhan pesat teknologi dan penetrasi internet yang semakin luas, platform *e-commerce* seperti Amazon telah menjadi salah satu destinasi utama bagi konsumen untuk berbelanja secara online. Menurut [serpwatch.io](https://serpwatch.io/blog/amazon-customer-demographics/) Aplikasi belanja seluler Amazon memiliki 150,6 juta pengguna pada tahun 2019. Pasar Amazon global memiliki 6,3 juta penjual. Selain itu, 85% konsumen muda membeli secara online setidaknya sekali seminggu. Dengan jutaan produk yang tersedia di platform tersebut, pengguna sering kali menghadapi tantangan dalam menavigasi melalui berbagai pilihan yang tersedia.

Masalah utama yang dihadapi oleh pengguna adalah kesulitan dalam menemukan produk yang sesuai dengan preferensi dan kebutuhan mereka. Sumber online [Alibaba.com](https://reads.alibaba.com/id/how-to-pick-winning-product-to-sell-on-amazon/#:~:text=Berjualan%20online%20terus%20menguntungkan%2C%20jadi,7%2C500%20produk%20terjual%20setiap%20menit.)  menyebutkan bahwa pada tahun 2021, mitra penjualan Amazon di AS menjual lebih dari 3.9 miliar produk dan rata-rata penjualan sekitar US$ 200,000. Seiring dengan meningkatnya jumlah produk, pengguna sering kali merasa overwhelmed dengan berbagai pilihan yang ada. Akibatnya, mereka mungkin memerlukan bantuan tambahan untuk menemukan produk yang relevan dan sesuai dengan preferensi mereka.

Dalam rangka meningkatkan pengalaman belanja pengguna dan meningkatkan retensi pelanggan, platform *e-commerce* seperti Amazon perlu mengimplementasikan sistem rekomendasi produk yang efektif. Sistem rekomendasi produk bertujuan untuk menyajikan produk-produk yang paling relevan dan menarik bagi setiap pengguna berdasarkan preferensi mereka, riwayat pembelian sebelumnya, perilaku penelusuran, dan faktor-faktor lainnya. Dalam mencari kemiripan penelitaian ini menggunakan metode cosine similarity untuk menghitung seberapa mirip setiap produk yang telah dibeli oleh pengguna berdasarkan deskripsi produk. Cosine similarity adalah metrik yang mengukur kemiripan antara dua vektor dengan mengukur kosinus sudut antara mereka di ruang multidimensi. Metode untuk sistem rekomendasi produk berdasarkan deskripsi produk ini menggunakan teknik *content-based filtering*.

## Business Understanding

### Problem Statements

Berdasarkan latar belakang diatas, berikut ini rumusan masalah yang dapat diselesaikan pada proyek ini:

1. Bagaimana cara melakukan pra-pemrosesan pada data penjualan amazone agar dapat membuat model yang baik menggunakan teknik content-base filtering?
2. Bagaimana memberikan rekomendasi produk berdasarkan deskripsi produk pada setiap produk yang telah dibeli oleh pelanggan?

### Goals

1. Melakukan pra-pemrosesan data dengan baik agar dapat digunakan dalam pembuatan model.
2. Membuat pelanggan lebih mudah menemukan produk yang tepat dengan bantuan sistem rekomendasi produk berdasarkan deskripsi produk yang telah dibeli.

### Solution statements
Solusi yang dapat dilakukan untuk memenuhi tujuan dari proyek ini diantaranya :

1. Melakukan pemrosesan data dengan beberapa teknik, yaitu :
   
   * Melakukan *Exploratory Data Analysis* untuk mengetahui persebaran, bentuk, dan jenis fitur pada dataset yang digunakan.
   * Melakukan pengecekan *missing value* agar data yang akan diproses memiliki kualitas yang baik.
     
2. Mengembangkan sistem rekomendasi dengan metode *Content Based Filtering*. *Content-based filtering* adalah pendekatan dalam sistem rekomendasi yang menggunakan informasi atau fitur dari item-item yang direkomendasikan untuk membuat prediksi atau rekomendasi. Pendekatan ini berfokus pada karakteristik atau fitur dari item itu sendiri dan mencocokkannya dengan preferensi atau profil pengguna. Metode ini bekerja dengan menyarankan item serupa yang pernah disukai sebelumnya atau sedang dilihat sekarang kepada pengguna berdasrakan kategori tertentu dari item yang dinilai oleh pengguna.

Keunggulan dari content-based filtering adalah kemampuannya untuk memberikan rekomendasi yang personal dan spesifik berdasarkan pada karakteristik dan preferensi pengguna. Ini juga tidak memerlukan data eksternal tentang pengguna atau interaksi antar pengguna. Namun, kelemahannya adalah keterbatasan dalam menemukan item-item yang baru atau tidak terduga, karena rekomendasi hanya didasarkan pada item-item yang memiliki fitur yang mirip dengan preferensi pengguna yang sudah diketahui.

## Data Understanding

Project ini menggunakan data yang bersumber pada sebuah situs kaggle, yaitu [Amazon Sales Dataset](https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset) dimana data tersebut memiliki dimensi 16 x 1464 dengan penjelasan fitur sebagai berikut :

- product_id - ID Produk
- product_name - Nama Produk
- category - Kategori Produk
- harga_diskon - Harga Diskon Produk
- harga_aktual - Harga Aktual Produk
- persentase_diskon - Persentase Diskon untuk Produk
- rating - Peringkat Produk
- rating_count - Jumlah orang yang memilih peringkat Amazon
- about_product - Deskripsi tentang Produk
- user_id - ID pengguna yang menulis ulasan untuk Produk
- user_name - Nama pengguna yang menulis ulasan untuk Produk
- review_id - ID dari ulasan pengguna
- revier_title - Ulasan singkat
- review_content - Ulasan panjang - Ulasan panjang
- img_link - Tautan Gambar Produk
- product_link - Tautan Situs Web Resmi Produk

## Data Visualisasi

### Distribusi Data
![Gambar 1. Distribusi Data](https://raw.githubusercontent.com/mufidatuln/Proyek-Sistem-Rekomendasi-Amazone-Product/main/aset/Gambar%201.%20Distribusi%20Data.PNG)

Berikut adalah visualisasi persebaran data numeric dari dataset produk amazone. Dapat dilihat pada fitur `discount_price`, `actual_price` dan `rating_count` memiliki distribusi data miring ke kanan.

Sedangka untuk fitur `discount_presentage` dan `rating` memilki distribusi hampir simetris

### Distribusi Produk Kategori Utama

![Gambar 2. Distribusi Produk Kategori Utama](https://raw.githubusercontent.com/mufidatuln/Proyek-Sistem-Rekomendasi-Amazone-Product/main/aset/Gambar%202.%20Distribusi%20Kategori%20Produk%20Utama.PNG)

Berdasarkan hasil tersebut dapat disimpulkan bahwa tiga kategori utama teratas adalah Elektronik, Komputer & Aksesori, dan Rumah & Dapur. Hal ini menunjukkan bahwa kategori-kategori ini populer di kalangan pelanggan. Jumlah produk dalam kategori utama lainnya cukup rendah, yang menunjukkan bahwa kategori-kategori ini tidak sepopuler tiga kategori teratas.

### Top Kategori Utama Berdasarkan Rating

![Gambar 3. Top Kategori Utama](https://raw.githubusercontent.com/mufidatuln/Proyek-Sistem-Rekomendasi-Amazone-Product/main/aset/Gambar%203.%20Top%20Kategori%20Utama%20Berdasarkan%20Rating.PNG)

Dengan melihat tabel ini, kita dapat melihat kategori utama yang diperingkat berdasarkan peringkat rata-rata. Kategori utama dengan peringkat tertinggi adalah Produk Kantor, Mainan & Permainan, dan Perbaikan Rumah, dengan peringkat di atas 4,0. Hal ini menunjukkan bahwa pelanggan pada umumnya puas dengan produk yang ditawarkan dalam kategori-kategori ini.

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.



