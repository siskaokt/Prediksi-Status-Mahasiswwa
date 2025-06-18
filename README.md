# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding
Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah berdiri sejak tahun 2000. Sejak berdirinya, institusi ini telah menghasilkan banyak lulusan dengan reputasi akademik yang baik. Namun, ada tantangan yang dihadapi institusi yaitu banyak mahasiswa yang tidak menyelesaikan studi alias dropout. Tingginya angka dropout ini berpotensi mencoreng reputasi institusi serta mengindikasikan permasalahan sistemik dalam proses pendidikan. Oleh karena itu, Jaya Jaya Institut ingin menerapkan sistem prediktif untuk mendeteksi mahasiswa yang berisiko dropout sejak awal dan memberi intervensi secara proaktif.

### Permasalahan Bisnis
Dari identifikasi awal, terdapat empat permasalahan utama yang ingin diselesaikan melalui proyek ini:
1. Tingginya jumlah mahasiswa dropout yang dapat menurunkan kualitas dan reputasi institusi.
2. Belum adanya sistem prediktif untuk mendeteksi mahasiswa yang berisiko dropout.
3. Minimnya insight analitik terkait faktor-faktor penyebab mahasiswa tidak menyelesaikan studi.
4. Ketiadaan dashboard pemantauan berbasis data untuk memudahkan monitoring performa mahasiswa.

### Cakupan Proyek
Untuk menjawab permasalahan di atas, proyek ini mencakup langkah-langkah berikut:
1. Melakukan Exploratory Data Analysis (EDA) untuk memahami karakteristik mahasiswa dan faktor penyebab dropout.
2. Membangun model machine learning untuk memprediksi status akhir mahasiswa.
3. Mengembangkan dashboard interaktif untuk menyajikan insight dan monitoring performa mahasiswa.

### Persiapan
Sumber data: Dataset diambil dari GitHub Dicoding sebagai bagian dari modul pelatihan, yang merupakan adaptasi dari dataset asli UCI Machine Learning Repository. Dataset ini juga dapat ditemukan dalam studi kasus resmi: Realinho, Valentim; Vieira Martins, Mónica; Machado, Jorge; dan Baptista, Luís. (2021). Predict students' dropout and academic success. [UCI Machine Learning Repository] https://doi.org/10.24432/C5MC89. 

## Setup Environment
Agar proyek ini dapat dijalankan secara lokal dengan lancar, berikut adalah tahapan setup environment:

1. Membuat virtual environment
python -m venv venv

2. Aktivasi virtual environment
   - Windows
   venv\Scripts\activate

   - Mac/Linux
   source venv/bin/activate

3. Menginstal Dependensi
   pip install --upgrade pip
   pip install -r requirements.txt

4. Menjalankan Skrip Utama
   Model ini memiliki dua komponen utama:
      1. Notebook: Eksplorasi dan model (modelling.ipynb)
      2. prediction.py: Simulasi prediksi karyawan
   Jalankan dengan perintah berikut:
   streamlit run prediction.py

## Business Dashboard
Dashboard Akademik telah dikembangkan menggunakan Looker Studio untuk menyajikan visualisasi data mahasiswa secara interaktif dan informatif. Adapun elemen utama dalam dashboard ini meliputi:
1. Distribusi Status Akhir Mahasiswa (Graduate, Dropout, Enrolled)
2. Rata-rata Nilai Masuk dan Jumlah Total Mahasiswa (ditampilkan dalam KPI box)
3. Hubungan antara Status Mahasiswa dengan Faktor Risiko, seperti:
   - Status Tunggakan Uang Kuliah
   - Adanya Hutang Pendidikan
   - Nilai Masuk Mahasiswa
4. Distribusi Jumlah Mata Kuliah yang Lulus pada Semester 1 dan Semester 2
5. Analisis Pekerjaan Orang Tua terhadap Status Mahasiswa
6. Filter Interaktif berdasarkan Jenis Kelamin, Status Beasiswa, dan Kebutuhan Khusus

Link dashboard bisa diakses [Dashboard] https://lookerstudio.google.com/reporting/01066d93-5eaa-49a2-9fef-37bb894672bb 

Dashboard ini bertujuan untuk membantu jaya jaya institut untuk:
1. Mengidentifikasi karakteristik umum mahasiswa yang berisiko dropout
2. Memonitor tren akademik dan beban studi mahasiswa
3. Mendukung pengambilan keputusan berbasis data melalui filter dan visualisasi yang mudah dipahami

## Model Machine Learning
Untuk menyelesaikan permasalahan ini, dibangun sebuah model machine learning untuk memprediksi apakah seorang karyawan memiliki kemungkinan untuk melakukan attrition (`Attrition = 1`). 2 algoritma yang telah diujicoba antara lain:
1. Logistic Regression
2. Random Forest Classifier 

Proses pengembangan dilakukan dengan tahapan:
1. Data understanding dan preparation, tahapan ini memahami karakteristik dari dataset dan memeriksa missing values serta data duplikat.
2. Data processing, tahapan ini melakukan encoding pada fitur kategorikal, membersihkan outlier pada dataset.
3. EDA, tahapan ini melakukan proses eksplor pada data, untuk menemukan faktor apa saja yang mempengaruhi dropout.
4. Data processing sebelum model, tahapan ini melakukan drop labeling untuk visualisasi dan SMOTE pada fitur y sebagai target karena terdapat imbalance data.
5. Modelling, tahapan ini membangun model dengan 2 algoritma, dan didapatkan model dengan peforma terbaik yaitu random forest.
6. Hyperparmeter tuning, tahapan ini melakukan tuning pada model random forest menggunakan gridsearchcv.
7. Save model, tahapan ini menyimpan model untuk proses deploy
8. Recommendation action, tahapan ini berisikan beberapa saran untuk institusi pendidikan 
9. Deployment, model ini mengasilkan antarmuka sederhana untuk memprediksi status mahasiswa dibangun menggunakan Streamlit untuk mendemonstrasikan bagaimana model dapat digunakan secara operasional.

Link aplikasi deployment dapat diakses di 

## Conclusion
Proyek ini bertujuan membantu institusi Jaya Jaya Institut dalam mengatasi tingginya tingkat dropout mahasiswa, yang berdampak negatif pada reputasi akademik dan efektivitas sistem pendidikan. Melalui tahapan analisis data dan pengembangan model prediktif berbasis machine learning, diperoleh hasil sebagai berikut:

1. Data mahasiswa berhasil dianalisis melalui tahap Exploratory Data Analysis (EDA), yang mengidentifikasi fitur-fitur penting seperti jumlah mata kuliah semester awal, status beasiswa, admission grade, hutang pendidikan, keterlambatan pembayaran UKT, serta pekerjaan orang tua sebagai faktor utama yang memengaruhi status akhir mahasiswa.

2. Berdasarkan hasil analisis EDA, karakteristik umum dari mahasiswa dengan risiko tinggi dropout antara lain:

Tidak memiliki beasiswa: Kelompok ini lebih banyak mengalami dropout dibanding penerima beasiswa.
Memiliki hutang pendidikan dan keterlambatan pembayaran UKT: Indikasi kesulitan finansial yang signifikan.
Nilai admission grade rendah: Prestasi awal yang rendah berkorelasi dengan kemungkinan tidak menyelesaikan studi.
Jumlah mata kuliah semester 1 dan 2 yang tidak lulus: Menunjukkan kesulitan akademik sejak awal.
Tidak adanya kebutuhan khusus atau dukungan tambahan: Mahasiswa dengan dukungan khusus justru menunjukkan tingkat kelulusan lebih tinggi.
Pekerjaan orang tua: Terkait dengan latar belakang sosial-ekonomi yang turut memengaruhi ketahanan studi.

3. Model prediktif berhasil dibangun dengan dua pendekatan:
   - Logistic Regression sebagai model uji coba.
   - Random Forest sebagai model utama, dengan performa terbaik setelah tuning.

4. Model Random Forest yang dituning menggunakan GridSearchCV menghasilkan:
Akurasi 85%

5. Sebuah dashboard interaktif telah dikembangkan menggunakan Looker Studio untuk menyajikan visualisasi performa mahasiswa secara efektif kepada tim akademik dan manajemen kampus.

Secara keseluruhan, proyek ini berhasil menjawab seluruh permasalahan bisnis yang diangkat di awal, serta memberikan landasan kuat bagi institusi dalam menyusun strategi intervensi akademik dan finansial secara proaktif untuk menurunkan angka dropout.

### Rekomendasi Action Items 
Berdasarkan hasil proyek ini, berikut tiga rekomendasi utama yang dapat dilakukan oleh pihak Jaya Jaya Institut:

1. Integrasi Model Prediktif ke Sistem Akademik
Model klasifikasi yang dikembangkan dapat digunakan untuk memonitor status mahasiswa aktif secara berkala. Terapkan model ke data mahasiswa aktif setiap awal semester untuk mendeteksi risiko dropout secara dini. Gunakan hasil prediksi untuk menargetkan intervensi seperti bimbingan belajar, konseling, atau bantuan keuangan.

2. Tindak Lanjut Berdasarkan Insight EDA
Insight dari EDA mengindikasikan bahwa faktor akademik dan finansial merupakan pemicu utama dropout. Prioritaskan dukungan kepada mahasiswa tanpa beasiswa, dengan hutang pendidikan, atau dengan prestasi akademik rendah. Evaluasi kembali kebijakan UKT, sistem cicilan, dan beban studi semester awal agar lebih adaptif terhadap kebutuhan mahasiswa.

3. Pemanfaatan Dashboard Interaktif untuk Pemantauan Rutin
Dashboard Looker Studio yang telah dikembangkan menyajikan visualisasi status mahasiswa dan indikator dropout dengan efektif. Gunakan dashboard secara mingguan/bulanan oleh tim akademik dan keuangan untuk mengidentifikasi area kritis. Libatkan dashboard dalam forum evaluasi akademik untuk pengambilan keputusan berbasis data secara kolaboratif antar divisi.