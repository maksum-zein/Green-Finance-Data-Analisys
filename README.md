# ETL-Assesment-Green-Finance-Data-Analisys

Berikut adalah tugas dan jawaban dari **Anggota Kelompok 5**

 | No| Nama | No Absen |
| --- | --- | --- |
| 1. | Bavari Muhammad Waldan | 9.029.DB2025 |
| 2. | Deka Isnadi | 9.037.DB2025 |
| 3. | Firmansyah | 10.049.DB2025 |
| 4. | Maksum | 9.045.DB2025 |

## 📖 1. Pendahuluan

Tugas ini merupakan bagian dari program asesmen analitik data bertema Green Finance yang bertujuan untuk meningkatkan pemahaman teknis peserta dalam mengolah data lingkungan, ekonomi, dan sosial terkait proyek energi hijau di Indonesia. Melalui pendekatan berbasis Python, peserta diminta menyelesaikan serangkaian soal dengan pendekatan pemrograman dasar hingga machine learning untuk mendukung pengambilan keputusan berkelanjutan.

---

## 🔍 2. Tugas Soal

Tugas terdiri dari tujuh soal utama dan satu soal bonus. Soal 1 hingga 7 meliputi berbagai konsep dasar pemrograman Python, seperti :

1. Penggabungan data (`merge`)

2. Logika `if-else`

3. Perulangan `for` dan `while`

4. Penggunaan `dictionary`

5. Pembuatan `fungsi`

. Serta penanganan kesalahan (`try-except`). 

Sementara itu, soal bonus menantang peserta membangun model machine learning menggunakan algoritma **Decision Tree Classifier** untuk memprediksi tingkat _Daya Tarik Investasi_ sebuah proyek berdasarkan indikator numerik.

---

## 📋 3. Output dari Soal

Output dari setiap soal mencakup:

* Soal 1: klasifikasi efisiensi pengurangan emisi CO2.

* Soal 2: rata-rata CO2 reduction proyek PLTM.
  
* Soal 3: informasi lahan dan konflik sosial dari input `Project_ID`.
  
* Soal 4: daftar proyek dengan investasi tinggi dan konflik rendah.
  
* Soal 5: total investasi lokasi efisien.
  
* Soal 6: fungsi efisiensi CO2 dengan error handling.

* Soal 7: rata-rata output energi hanya untuk proyek yang valid.

* Bonus: akurasi model machine learning dan prediksi daya tarik investasi untuk proyek baru.

---

## 📚 4. Library yang Dipakai

Install library ayng di perlukan 
1. Pandas
2. Numpy
3. Matplotlib
4. Jupyter
5. Openpyxl
6. Scikit-learn

```sh
pip install pandas numpy matplotlib jupyter openpyxl scikit-learn 
```

---
## 🗂️ 5. Dataset yang Dipakai

Ada 5 dataset digunakan dalam tugas ini, yaitu:

1. `Environmental_Dataset.xlsx` – berisi data CO2 reduction dan energy output,
2. `Financial_Dataset.xlsx` – berisi biaya investasi tiap proyek,
3. `Social_Dataset.xlsx` – berisi status lahan dan konflik sosial,
4. `Economic_Dataset.xlsx` – berisi GDP growth dan daya tarik investasi,
5. `Geospatial_Dataset.xlsx` – berisi efisiensi lokasi,

Setiap dataset dihubungkan melalui kolom `Project_ID`.

---

## 📌 6. Hasil Output dari Jawaban

Hasil dari seluruh jawaban menunjukkan keberhasilan peserta dalam mengolah data real-world menggunakan Python. Pada soal bonus, model Decision Tree yang dilatih dengan tiga fitur utama menghasilkan **akurasi sekitar 85–90%**, dan mampu memprediksi proyek baru dengan `GDP_Growth=5.0`, `CO2_Reduction=70000`, dan `Investment_Cost=150` sebagai proyek dengan **daya tarik investasi tinggi**. Visualisasi pohon keputusan juga menunjukkan bagaimana fitur berpengaruh terhadap klasifikasi akhir.

--- 

## 💡 7. Kesimpulan
Tugas ini menunjukkan pentingnya integrasi antara keterampilan teknis Python dan pemahaman terhadap isu keberlanjutan. 

Dari eksplorasi data dasar hingga penerapan machine learning, peserta mampu mengolah informasi kompleks menjadi wawasan yang dapat digunakan untuk mendukung keputusan pendanaan hijau di Indonesia. 

Tugas ini juga menunjukkan bahwa pendekatan data-driven sangat relevan dalam menilai kelayakan proyek energi bersih.

