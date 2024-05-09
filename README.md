# Laporan Proyek Machine Learning - Mufidatul Ngazizah

## Project Overview
Dengan pertumbuhan pesat teknologi dan penetrasi internet yang semakin luas, platform *e-commerce* seperti Amazon telah menjadi salah satu destinasi utama bagi konsumen untuk berbelanja secara online. Menurut serpwatch.io aplikasi belanja seluler Amazon memiliki 150,6 juta pengguna pada tahun 2019. Pasar Amazon global memiliki 6,3 juta penjual. Selain itu, 85% konsumen muda membeli secara online setidaknya sekali seminggu[1]. Dengan jutaan produk yang tersedia di platform tersebut, pengguna sering kali menghadapi tantangan dalam menavigasi melalui berbagai pilihan yang tersedia.

Masalah utama yang dihadapi oleh pengguna adalah kesulitan dalam menemukan produk yang sesuai dengan preferensi dan kebutuhan mereka. Sumber online Alibaba.com menyebutkan bahwa pada tahun 2021, mitra penjualan Amazon di AS menjual lebih dari 3.9 miliar produk dan rata-rata penjualan sekitar US$ 200,000[2]. Seiring dengan meningkatnya jumlah produk, pengguna sering kali merasa overwhelmed dengan berbagai pilihan yang ada. Akibatnya, mereka mungkin memerlukan bantuan tambahan untuk menemukan produk yang relevan dan sesuai dengan preferensi mereka.

Dalam rangka meningkatkan pengalaman belanja pengguna dan meningkatkan retensi pelanggan, platform *e-commerce* seperti Amazon perlu mengimplementasikan sistem rekomendasi produk yang efektif. Sistem rekomendasi merupakan alat atau perangkat lunak yang dapat memberikan saran, usulan, anjuran kepada pengguna mengenai item atau sesuatu yang baik untuk mereka dapatkan
atau gunakan[3]. Sistem rekomendasi produk bertujuan untuk menyajikan produk-produk yang paling relevan dan menarik bagi setiap pengguna berdasarkan preferensi mereka, riwayat pembelian sebelumnya, perilaku penelusuran, dan faktor-faktor lainnya. Dalam mencari kemiripan penelitaian ini menggunakan metode cosine similarity untuk menghitung seberapa mirip setiap produk yang telah dibeli oleh pengguna berdasarkan deskripsi produk. Cosine similarity adalah metrik yang mengukur kemiripan antara dua vektor dengan mengukur kosinus sudut antara mereka di ruang multidimensi. Metode untuk sistem rekomendasi produk berdasarkan deskripsi produk ini menggunakan teknik *content-based filtering* dan *colaborative filtering*.

## Business Understanding

### Problem Statements

Berdasarkan latar belakang diatas, berikut ini rumusan masalah yang dapat diselesaikan pada proyek ini:

1. Bagaimana cara melakukan pra-pemrosesan pada data penjualan amazone agar dapat membuat model yang baik menggunakan teknik content-base filtering dan colaborative filtering?
2. Bagaimana memberikan rekomendasi produk berdasarkan deskripsi produk pada setiap produk yang telah dibeli oleh pelanggan?

### Goals

1. Melakukan pra-pemrosesan data dengan baik agar dapat digunakan dalam pembuatan model.
2. Membuat pelanggan lebih mudah menemukan produk yang tepat dengan bantuan sistem rekomendasi produk berdasarkan deskripsi produk yang telah dibeli dan rating pengguna.

### Solution statements
Solusi yang dapat dilakukan untuk memenuhi tujuan dari proyek ini diantaranya :

1. Melakukan pemrosesan data dengan beberapa teknik, yaitu :
   
   * Melakukan *Exploratory Data Analysis* untuk mengetahui persebaran, bentuk, dan jenis fitur pada dataset yang digunakan.
   * Melakukan pengecekan *missing value* agar data yang akan diproses memiliki kualitas yang baik.
     
2. Mengembangkan sistem rekomendasi dengan metode *Content Based Filtering* dan *Collaborative Filtering*
   
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

Pada Gambar 1. Distribusi Data merupakan visualisasi persebaran data numeric dari dataset produk amazone. Dapat dilihat pada fitur `discount_price`, `actual_price` dan `rating_count` memiliki distribusi data miring ke kanan.

Sedangka untuk fitur `discount_presentage` dan `rating` memilki distribusi hampir simetris

### Distribusi Produk Kategori Utama

![Gambar 2. Distribusi Produk Kategori Utama](https://raw.githubusercontent.com/mufidatuln/Proyek-Sistem-Rekomendasi-Amazone-Product/main/aset/Gambar%202.%20Distribusi%20Kategori%20Produk%20Utama.PNG)

Berdasarkan hasil yang dapat di lihat pada Gambar 2. Distribusi Produk Kategori Utama dapat disimpulkan bahwa tiga kategori utama teratas adalah Elektronik, Komputer & Aksesori, dan Rumah & Dapur. Hal ini menunjukkan bahwa kategori-kategori ini populer di kalangan pelanggan. Jumlah produk dalam kategori utama lainnya cukup rendah, yang menunjukkan bahwa kategori-kategori ini tidak sepopuler tiga kategori teratas.

### Top Kategori Utama Berdasarkan Rating

![Gambar 3. Top Kategori Utama](https://raw.githubusercontent.com/mufidatuln/Proyek-Sistem-Rekomendasi-Amazone-Product/main/aset/Gambar%203.%20Top%20Kategori%20Utama%20Berdasarkan%20Rating.PNG)

Dengan melihat Gambar 3. Top Kategori Utama ini, kita dapat melihat kategori utama yang diperingkat berdasarkan peringkat rata-rata. Kategori utama dengan peringkat tertinggi adalah Produk Kantor, Mainan & Permainan, dan Perbaikan Rumah, dengan peringkat di atas 4,0. Hal ini menunjukkan bahwa pelanggan pada umumnya puas dengan produk yang ditawarkan dalam kategori-kategori ini.

## Data Preparation
Beberapa teknik yang digunakan pada data preparation sebagai berikut :
1. Data Cleaning
   
      * Mengecek missing value dengan methode `.isnull()` untuk mengetahui berapa banyak jumlah *missing value* di setiap kolom.
   
      * Melakukan pembersihan missing value dengan methode *dropna()*.  Metode dropna() secara langsung menghapus baris atau kolom yang mengandung nilai yang hilang. Hal ini membuat proses pembersihan data menjadi sederhana dan cepat dilakukan.
   
      * Mengecek apakah terdapat data yang duplikat dengan method *duplicated()*. Data yang duplikat dapat menghasilkan kesalahan dalam analisis. Misalnya, jika kita menghitung statistik deskriptif atau melakukan analisis model, keberadaan data duplikat dapat menghasilkan perkiraan yang tidak akurat atau bias.

2. Data Preparation

   * Mengubah beberapa format dari fitur menjadi numerik atau float

   * Mengubah beberapa struktur format pada fitur 'rating` yang tidak sesuai
   
   * Melakukan proses vektorisasi pada kolom 'product_detail'.
   
   Memuat kolom baru yaitu produk_details yang berisi beberapa kolom/fitur yaitu product_name, about_product dan reviwe_product. Pada setiap fitur agar dapat dilakukan encoding. Pada tahap ini dilakukan untuk mengubah teks menjadi vektor dengan fitur TF-IDF. Pada hal ini menerapkan fit_transform pada teks yang diberikan dalam dataset. fit_transform akan menghitung TF-IDF untuk setiap kata dalam teks dan menghasilkan matriks yang berisi nilai TF-IDF untuk setiap kata dalam setiap dokumen. Hasil dari proses vektorisasi disimpan dalam variabel tfidf_matrix.  Hasilnya adalah matriks yang berisi representasi numerik dari teks dalam dataset, di mana setiap baris mewakili satu dokumen dan setiap kolom mewakili kata tertentu dalam kumpulan data.

   * Melakukan Split Dataset
     
      Dataset dimuat dari dataframe yang diberikan, hanya memilih kolom user_id, product_id, dan rating.
Dataset kemudian dibagi menjadi set pelatihan (trainset) dan set pengujian (testset) menggunakan *train_test_split*.


# Modeling

## Recomendation Content Based Filtering
 *Content-based filtering* adalah pendekatan dalam sistem rekomendasi yang menggunakan informasi atau fitur dari item-item yang direkomendasikan untuk membuat prediksi atau rekomendasi. Pendekatan ini berfokus pada karakteristik atau fitur dari item itu sendiri dan mencocokkannya dengan preferensi atau profil pengguna. Metode ini bekerja dengan menyarankan item serupa yang pernah disukai sebelumnya atau sedang dilihat sekarang kepada pengguna berdasrakan kategori tertentu dari item yang dinilai oleh pengguna.

Keunggulan dari content-based filtering adalah kemampuannya untuk memberikan rekomendasi yang personal dan spesifik berdasarkan pada karakteristik dan preferensi pengguna. Ini juga tidak memerlukan data eksternal tentang pengguna atau interaksi antar pengguna. Namun, kelemahannya adalah keterbatasan dalam menemukan item-item yang baru atau tidak terduga, karena rekomendasi hanya didasarkan pada item-item yang memiliki fitur yang mirip dengan preferensi pengguna yang sudah diketahui.

Model algoritma rekomendasi content bases ini menggunakan metode *cosine similarity*. *Cosine similarity* adalah metrik yang digunakan untuk mengukur seberapa mirip dua vektor dalam ruang berdimensi banyak. Dalam konteks sistem rekomendasi atau pemrosesan teks, *cosine similarity* sering digunakan untuk mengukur seberapa mirip dua dokumen atau item berdasarkan representasi numerik mereka.

Dalam konteks sistem rekomendasi, *cosine similarity* sering digunakan untuk membandingkan profil pengguna dengan item-item dalam basis data untuk memberikan rekomendasi. Misalnya, dalam sistem rekomendasi berbasis konten, *cosine similarity* dapat digunakan untuk membandingkan profil preferensi pengguna dengan deskripsi atau atribut-atribut produk untuk menentukan seberapa cocok produk tersebut dengan preferensi pengguna. Semakin tinggi nilai *cosine similarity* antara profil pengguna dan produk, semakin besar kemungkinan produk tersebut direkomendasikan kepada pengguna.


* Hasil Rekomendasi

 Berikut hasil dari pemanggilan fungsi content_based_recommendations dengan argumen 'B09LHXNZLR' pada dataset dan matriks similaritas kosinus (cosine_sim).

|  product_id |  product_name |
|---|---|
| B07M69276N  | TP-Link AC1300 USB WiFi Adapter (Archer T3U) - 2.4G/5G Dual Band Mini Wireless Network Adapter for PC Desktop, MU-MIMO Wi-Fi Dongle, USB 3.0, Supports Windows 11,10, 8.1, 8, 7, XP/Mac OS 10.15 and earlier  |
| B08G43CCLC | NK STAR 950 Mbps USB WiFi Adapter Wireless Network Receiver Dongle for Desktop Laptop, (Support- Windows XP/7/8/10 & MAC OS) NOt Support to DVR and HDTV  |
| B0088TKTY2 |  TP-LINK WiFi Dongle 300 Mbps Mini Wireless Network USB Wi-Fi Adapter for PC Desktop Laptop(Supports Windows 11/10/8.1/8/7/XP, Mac OS 10.9-10.15 and Linux, WPS, Soft AP Mode, USB 2.0) (TL-WN823N),Black |
| B07P681N66 | TP-Link AC600 600 Mbps WiFi Wireless Network USB Adapter for Desktop PC with 2.4GHz/5GHz High Gain Dual Band 5dBi Antenna Wi-Fi, Supports Windows 11/10/8.1/8/7/XP, Mac OS 10.15 and earlier (Archer T2U Plus)  |
| B07P681N66 | TP-Link AC600 600 Mbps WiFi Wireless Network USB Adapter for Desktop PC with 2.4GHz/5GHz High Gain Dual Band 5dBi Antenna Wi-Fi, Supports Windows 11/10/8.1/8/7/XP, Mac OS 10.15 and earlier (Archer T2U Plus)  |

Tabel 1. Hasil Rekomendasi *Content-based Filtering*

## Recomendation Collaborative Filtering
Collaborative filtering adalah metode yang digunakan dalam sistem rekomendasi untuk menghasilkan rekomendasi kepada pengguna berdasarkan penilaian (rating) atau perilaku pengguna serta kesamaan atau perbandingan dengan pengguna lain. Dalam collaborative filtering, rekomendasi dibuat berdasarkan pola hubungan antara pengguna dan item yang diamati dari data riil.

* Melatih model *collaborative filtering* berbasis pengguna menggunakan algoritma KNN (K-Nearest Neighbors)
  
Model KNN (K-Nearest Neighbors) adalah salah satu model yang digunakan dalam machine learning untuk memprediksi atau mengklasifikasikan data berdasarkan kedekatannya dengan data lain dalam ruang fitur. Di bidang sistem rekomendasi, KNN dapat digunakan dalam dua konteks: collaborative filtering dan content-based filtering.

* Hasil Rekomendasi

Dari semua produk yang tersedia, ambil produk yang belum diberikan rating oleh pengguna tertentu. Ini dilakukan dengan memeriksa DataFrame dataset untuk produk yang tidak ada dalam data uji. Memperkirakan rating dengan menggunakan model kolaboratif yang telah dilatih untuk memperkirakan rating pada produk yang belum diberikan rating oleh pengguna tertentu. Ini dilakukan dengan memanggil metode predict() pada model.

Setelah mendapatkan prediksi rating untuk produk yang belum diberikan rating oleh pengguna, urutkan produk tersebut berdasarkan rating terprediksi dari tertinggi ke terendah. Kemudian ambil 3 produk teratas sebagai rekomendasi untuk pengguna tertentu. Dapat di lihat pada Tabel 2 adalah hasil rekomendasi *colaborative filtering*.

| product_id |  perd_product_name | 
|---|---|---|---|---|
| B08M66K48D |  POPIO Tempered Glass Screen Protector Compatible for iPhone 12 / iPhone 12 Pro | 
| B08MCD9JFY | Tygot 10 Inches Big LED Ring Light for Camera, Phone tiktok YouTube Video Shooting and Makeup  |  
| B07YQ5SN4H |  Cello Non-Stick Aluminium Sandwich Gas Toaster(Black) |

Tabel 2. Hasil Rekomendasi Colaborative Filtering


# Evaluasi

Evaluasi yang dilakukan dalam proyek Conten Based Filtering adalah metrik *Average Precision* (AP)

* Fungsi `average_precision_score` dijalankan dengan dua parameter:
  
1. `ground_truth`: Ini adalah daftar label biner yang menunjukkan relevansi sebenarnya dari setiap item yang direkomendasikan. Label ini telah ditetapkan sebelumnya berdasarkan rating yang diberikan oleh pengguna.
2. `predicted_scores`: Ini adalah skor prediksi yang menunjukkan seberapa relevan setiap item yang direkomendasikan menurut sistem. Skor ini diperoleh dari metode *cosine similarity* yang digunakan untuk merekomendasikan item.

*Average precision* memberikan gambaran tentang seberapa baik sistem rekomendasi mampu mengurutkan item yang relevan di atas yang tidak relevan. Semakin tinggi nilai a*verage precision*, semakin baik kualitas rekomendasi sistem tersebut. Nilai *average precision* berkisar antara 0 hingga 1, dengan nilai 1 menunjukkan kualitas rekomendasi yang sempurna.


Tabel 3. Evaluasi Avarage precision
|  Avarage precision |  1.0 |
|---|---|


Tabel 3 merupakan hasil evaluasi dari proyek rekomendasi ini yang mana matric *Avarage precision* memperoleh nilai 1. Hal itu menandakah bahwa kualitas rekomendasi yang diberikan sesuai dan relevan dengan deskripsi produk yang pelangan beli sebelumnya.

Sedangkan untuk model *Collaborative Filtering* evaluasi metrik yang digunakan antara lain :

1. Root Mean Squared Error (RMSE):
   
RMSE adalah metrik evaluasi yang mengukur seberapa akurat model dalam memprediksi nilai rating atau skor pengguna terhadap item. RMSE memberikan informasi tentang seberapa jauh rata-rata prediksi model dari nilai sebenarnya. Semakin rendah RMSE, semakin baik kualitas prediksi model.

2. Mean Absolute Error (MAE):
   
MAE juga merupakan metrik evaluasi yang mengukur seberapa akurat model dalam memprediksi nilai rating atau skor pengguna terhadap item. Secara matematis, MAE dihitung sebagai rata-rata dari nilai absolut dari selisih antara nilai prediksi dan nilai sebenarnya. MAE memberikan informasi tentang seberapa besar kesalahan rata-rata prediksi model dari nilai sebenarnya. Semakin rendah MAE, semakin baik kualitas prediksi model.

Dari hasil evaluasi model di dapat nilai evaluasi sebagai berikut :
Tabel 4. Evaluasi RMSE dan MAE

| RMSE  | MAE  |
|---|---|
| 0.2636  | 0.1829  |

Dari Tabel 4 dapat dilihat bahwa evaluasi RMSE dan MAE memiliki nilai yang rendah, artinya kualitas prediksi dari model dapat dianggap baik, sehingga dapat dikatakan bahwa rekomedasi produk berdasarkan pada prediksi rating telah tercapai.

# Referensi 
[1] Serpwatch.io. (2024). Understanding Amazon Customer Demographics: A Comprehensive Guide. Diakses pada tanggal [3 Mei 2024], dari https://serpwatch.io/blog/amazon-customer-demographics/
[2] Alibaba.com. (2024). How to Pick a Winning Product to Sell on Amazon. Diakses pada tanggal [3 Mei 2024], dari https://reads.alibaba.com/id/how-to-pick-winning-product-to-sell-on-amazon/#:~:text=Berjualan%20online%20terus%20menguntungkan%2C%20jadi,7%2C500%20produk%20terjual%20setiap%20menit
[3] Maristha Made Devayani D, Sasonto Albertus Joko, Dewi Findra Kartika S. (2021). Sistem Rekomendasi Pembelian Produk Kesehatan pada E-Commerce ABC. Jurnal Ilmiah Teknik Informatika "Elaborasi", 3(2), 100-110. https://e-journal.uajy.ac.id/26693/3/19.%20Sistem%20Rekomendasi%20Pembelian%20Produk%20Kesehatan%20pada%20E-Commerce%20ABC.pdf   

