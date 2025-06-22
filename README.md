# Proyek Akhir: Menyelesaikan Permasalahan Jaya Jaya Institut

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

Berikut adalah dashboard yang bisa diakses secara online : [Dashboard](https://penerapan-data-science-proyek-akhir-m99gluj6a9eqcqitxeodjm.streamlit.app/)

## Menjalankan Sistem Machine Learning
Proyek ini juga menyediakan sistem **prediksi dropout mahasiswa berbasis web** menggunakan **Streamlit**.

### Cara Menjalankan Prototype:

```bash
# Jalankan aplikasi web secara local
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
Berikut adalah dashboard yang bisa diakses secara online : [Dashboard](https://penerapan-data-science-proyek-akhir-m99gluj6a9eqcqitxeodjm.streamlit.app/)

## Conclusion
| No | Fitur                                | Korelasi Terhadap Target |
|----|--------------------------------------|----------------------------|
| 1  | Age_at_enrollment                    | 0.254215                   |
| 2  | Curricular_units_1st_sem_approved    | -0.479112                  |
| 3  | Curricular_units_1st_sem_grade       | -0.480669                  |
| 4  | Curricular_units_2nd_sem_approved    | -0.569500                  |
| 5  | Curricular_units_2nd_sem_grade       | -0.571792                  |

Berdasarkan hasil analisis data dan pemodelan prediksi dropout mahasiswa, ditemukan beberapa fitur yang memiliki korelasi kuat terhadap status dropout. Fitur-fitur numerik seperti `Curricular_units_2nd_sem_grade`, `Curricular_units_2nd_sem_approved`, serta `Curricular_units_1st_sem_grade` dan `Curricular_units_1st_sem_approved` memiliki korelasi negatif yang cukup tinggi terhadap target, menunjukkan bahwa semakin rendah performa akademik mahasiswa, semakin besar kemungkinan mereka untuk dropout.

| No | Fitur                   | Korelasi terhadap Target |
|----|-------------------------|----------------------------|
| 1  | Tuition_fees_up_to_date | 0.428187                   |
| 2  | Application_mode        | 0.293925                   |
| 3  | Course                  | 0.252620                   |
| 4  | Scholarship_holder      | 0.244359                   |
| 5  | Debtor                  | 0.228176                   |
| 6  | Previous_qualification  | 0.205406                   |
| 7  | Gender                  | 0.202942                   |

Sementara itu, fitur kategorikal seperti `Tuition_fees_up_to_date`, `Application_mode`, dan `Scholarship_holder` juga menunjukkan korelasi positif yang cukup signifikan terhadap status dropout, menandakan adanya faktor non-akademik seperti kondisi finansial dan proses awal pendaftaran yang turut memengaruhi tingkat dropout.

Dari segi pemodelan, model **Logistic Regression** menunjukkan performa terbaik dalam memprediksi mahasiswa yang akan dropout, dengan jumlah prediksi benar sebanyak **228 siswa**, mengungguli Random Forest dan Decision Tree. Oleh karena itu, model ini dipilih sebagai model utama untuk sistem prediksi dropout mahasiswa.

### Rekomendasi Action Items
Untuk menurunkan tingkat dropout mahasiswa, berikut beberapa rekomendasi langkah yang dapat diambil oleh institusi pendidikan:

* **Melakukan intervensi dini terhadap mahasiswa dengan performa akademik rendah**, terutama yang memiliki nilai dan jumlah mata kuliah lulus di semester pertama dan kedua yang sedikit. Program mentoring dan remedial dapat menjadi solusi preventif.

* **Menindaklanjuti mahasiswa yang belum melunasi tuition fees atau menunjukkan gejala masalah finansial**, dengan menawarkan program bantuan keuangan, beasiswa tambahan, atau keringanan pembayaran.

* **Melakukan profiling terhadap mahasiswa berdasarkan jalur pendaftaran (Application\_mode)**, untuk mengidentifikasi apakah jalur tertentu cenderung memiliki risiko dropout lebih tinggi, lalu mengoptimalkan proses seleksi dan pembinaan awal.

* **Mengembangkan dashboard monitoring dan model prediksi dropout internal** berbasis model Logistic Regression yang telah dibuat untuk membantu pihak manajemen kampus mengidentifikasi risiko dropout mahasiswa secara otomatis dan berkala.
