# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan dikenal telah mencetak banyak lulusan berprestasi. Namun, dalam beberapa tahun terakhir, angka mahasiswa yang tidak menyelesaikan studi alias dropout semakin meningkat. Hal ini menimbulkan kekhawatiran terhadap citra institusi dan kualitas layanannya.

Sebagai bentuk pencegahan, pihak manajemen ingin memiliki sistem prediksi dropout mahasiswa agar dapat memberikan intervensi atau bimbingan khusus sejak dini. Untuk itu, mereka bekerja sama dengan tim data science untuk membangun sistem berbasis data dan machine learning.
### Permasalahan Bisnis
- Tingginya angka dropout mahasiswa di berbagai program studi.

- Belum adanya alat bantu prediksi berbasis data untuk mengidentifikasi mahasiswa berisiko tinggi.

- Kebutuhan untuk memahami faktor-faktor utama yang memengaruhi keputusan mahasiswa untuk dropout.

### Cakupan Proyek
- Melakukan eksplorasi dan analisis data dari dataset yang telah disediakan.

- Membangun dashboard visual untuk memantau status mahasiswa dan insight dari data.

- Mengembangkan model machine learning yang mampu memprediksi kemungkinan mahasiswa akan dropout.

- Menyediakan prototype aplikasi web untuk digunakan oleh pihak institusi dalam proses monitoring dan prediksi.

### Persiapan

Sumber data: [Dataset](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

Setup environment:
```bash
# Install dependency
pip install -r requirements.txt
```

## Business Dashboard
Dashboard yang dikembangkan dalam proyek ini bertujuan untuk memberikan wawasan yang mudah dipahami oleh manajemen **Jaya Jaya Institut** mengenai data mahasiswa dan potensi dropout.

### Fitur Utama Dashboard:

1. **Ikhtisar Dropout Mahasiswa**
   Menampilkan total mahasiswa, jumlah dropout, dan persentase dropout dalam bentuk metrik dan grafik perbandingan status mahasiswa (Dropout vs Bertahan).

2. **Visualisasi Fitur Kategorikal**

   * Menyajikan distribusi status mahasiswa terhadap fitur kategorikal seperti *Tuition\_fees\_up\_to\_date*, *Application\_mode*, *Course*, *Gender*, dll.
   * Untuk fitur dengan banyak kategori (seperti *Course* dan *Application\_mode*), hanya **top 5 kategori dengan dropout terbanyak** yang divisualisasikan agar tetap informatif.

3. **Visualisasi Fitur Numerikal**

   * Menampilkan hubungan antara fitur numerikal dengan tingkat dropout.
   * Fitur numerikal seperti *nilai* dan *jumlah unit yang disetujui* dikelompokkan ke dalam **kuartil** (binning) untuk memperjelas pola.
   * Visualisasi dropout rate dalam bentuk **bar chart** atau **line plot** tergantung jenis fitur.

Dashboard ini dapat digunakan sebagai alat bantu monitoring berkala oleh pihak institusi dalam mengidentifikasi pola dropout dan pengambilan keputusan berbasis data.

## Menjalankan Sistem Machine Learning
Proyek ini juga menyediakan sistem **prediksi dropout mahasiswa berbasis web** menggunakan **Streamlit**.

### Cara Menjalankan Prototype:

```bash
# Jalankan aplikasi web
streamlit run app.py
```

Setelah dijalankan, aplikasi akan terbuka di browser. Di bagian "Prediksi Dropout", pengguna dapat mengisi informasi mahasiswa seperti:

* Status pembayaran kuliah
* Mode aplikasi
* Program studi
* Penerima beasiswa atau tidak
* Status hutang
* Kualifikasi sebelumnya
* Gender
* Usia saat pendaftaran
* Nilai dan jumlah unit yang disetujui pada semester 1 dan 2

Setelah mengisi form, sistem akan memprediksi apakah mahasiswa tersebut **berpotensi dropout atau bertahan**, lengkap dengan **probabilitasnya**.

Contoh hasil:

```bash
Prediksi: Dropout
Probabilitas Dropout: 78.72%
Probabilitas Bertahan: 21.28%
```

Sistem ini juga dapat digunakan sebagai alat onboarding untuk mengidentifikasi mahasiswa baru yang berisiko tinggi dan segera diberi bimbingan khusus.

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
