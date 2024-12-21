# 🌟 **ADIKARA 2024 - Data Mining Competition**

![ADIKARA 2024 Banner](https://github.com/Arfazrll/AllReference/blob/main/Adikara.image.header.png?raw=true)

**ADIKARA 2024 - Data Mining Competition**! 🏆 
Kompetisi ini bertujuan untuk mengasah keterampilan analisis data mahasiswa dalam memprediksi **Food Price Index** dengan dataset spatiotemporal.

---

## 📋 **Daftar Isi**

- [🌟 Latar Belakang](#-latar-belakang)
- [🎯 Tujuan](#-tujuan)
- [📂 Struktur Repository](#-struktur-repository)
- [📊 Dataset](#-dataset)
- [📏 Metrik Evaluasi](#-metrik-evaluasi)
- [🚀 Alur Penyelesaian](#-alur-penyelesaian)
- [📘 Notebook 1 - Pelatihan Model](#-notebook-1---pelatihan-model)
- [📗 Notebook 2 - Prediksi Submission](#-notebook-2---prediksi-submission)
- [📑 Format Submission](#-format-submission)
- [💻 Cara Menjalankan](#-cara-menjalankan)
-  [🛠️ Prasyarat](#%EF%B8%8F-prasyarat)
- [📂 File Pendukung](#-file-pendukung)
- [🌐 Teknologi yang Digunakan](#-teknologi-yang-digunakan)

---

## 🌟 **Latar Belakang**
Untuk membaca, menganalitis dan menangani data spatiotemporal. Dengan dataset berbasis **indeks harga pangan**, lalu mengembangkan model yang mendukung pengambilan keputusan terkait data tersebut.

---

## 🎯 **Tujuan**
- **Mengaplikasikan Data dan Machine Learning**
- **Meningkatkan teknis dalam data mining**
- **Mendukung pengambilan keputusan berbasis data**

---

## 📂 **Struktur Repository**

```plaintext
adikara2024-datamining/
├── Notebook File/
│   ├── Notebook1_Manusia_Pelupa_ADIKARA2024.ipynb
│   └── Notebook2_Manusia_Pelupa_ADIKARA2024.ipynb
├── Submission File/
│   ├── submission_Manusia Pelupa_ADIKARA2024.csv
│   └── test_adikara2024_unlabeled.csv
├── adikara2024-datamining/
│   ├── train_adikara2024.csv
│   └── sample_submission_adikara2024.csv
├── LICENSE
├── README.md
└── ...
```

---

## 📊 **Dataset**

| **File**                   | **Deskripsi**                                                |
|----------------------------|------------------------------------------------------------|
| `train_adikara2024.csv`    | Data pelatihan dengan label *Food Price Index*              |
| `test_adikara2024_unlabeled.csv` | Data uji tanpa label, digunakan untuk prediksi                 |
| `sample_submission_adikara2024.csv` | Contoh format file *submission* untuk leaderboard            |

> ⚠️ **Catatan:** Pastikan untuk Menggunakan data dengan benar.

---

## 📏 **Metrik Evaluasi**
Menggunakan **Symmetric Mean Absolute Percentage Error (sMAPE)**:

![sMAPE Formula](https://github.com/Arfazrll/AllReference/blob/main/sMape.png)

Semakin **kecil nilai sMAPE**, semakin baik prediksi modelnya.

---

## 🚀 **Alur Penyelesaian**

1. 📥 **Eksplorasi Data**
2. 🛠️ **Pre-processing & Feature Engineering**
3. 🧠 **Pemodelan**
4. 📊 **Evaluasi Model dengan sMAPE**
5. 💾 **Eksport Model Terbaik**
6. 🔍 **Prediksi Data Uji**
7. 📝 **Generate Submission File**

---

## 📘 **Notebook 1 - Pelatihan Model**
**Nama File:** `Notebook1_NamaTim_ADIKARA2024.ipynb`

Notebook ini mencakup:
- Eksplorasi data (`train_adikara2024.csv`)
- *Pre-processing* (menangani nilai hilang, *encoding*, dsb.)
- Pelatihan model dengan algoritma seperti Random Forest, XGBoost, dll.
- Evaluasi model menggunakan sMAPE
- Eksport model terbaik (`Model_NamaTim_ADIKARA2024`)

---

## 📗 **Notebook 2 - Prediksi Submission**
**Nama File:** `Notebook2_NamaTim_ADIKARA2024.ipynb`

Notebook ini mencakup:
- Membaca file `test_adikara2024_unlabeled.csv`
- Mengimpor model terbaik dari Notebook 1
- *Pre-processing* data uji
- Memprediksi *Food Price Index*
- Menghasilkan file submission (`submission_NamaTim_ADIKARA2024.csv`)

---

## 📑 **Format Submission**

Berikut format yang harus digunakan untuk file submission:

```csv
id,FoodPriceIndex
122,20.5
123,21.7
124,19.8
```

---

## 💻 **Cara Menjalankan**

1. Clone repository ini:
   ```bash
   git clone https://github.com/YourUsername/adikara2024-datamining.git
   cd adikara2024-datamining
   ```

2. Siapkan lingkungan Python (opsional):
   ```bash
   python -m venv env
   source env/bin/activate  # Untuk Linux/Mac
   env\Scripts\activate   # Untuk Windows
   pip install -r requirements.txt
   ```

## 🛠️ **Prasyarat**

Pastikan Anda memiliki:
- Python 3.8 atau lebih baru
- Library utama seperti `pandas`, `numpy`, `scikit-learn`, `xgboost`, dll.
- Jupyter Notebook untuk menjalankan `.ipynb` file

---

## 📂 **File Pendukung**

| **File/Fungsi**          | **Deskripsi** |
|--------------------------|---------------|
| `requirements.txt`       | Daftar library yang diperlukan untuk menjalankan kode |
| `sample_submission.csv`  | Template untuk format submission |
| `train.csv`              | Dataset pelatihan dengan label |
| `test.csv`               | Dataset uji tanpa label |

---

## 🌐 **Teknologi yang Digunakan**

- Python 🐍
- Jupyter Notebook 📓
- Machine Learning (Random Forest, XGBoost, dll.) 🤖
- Pandas & Numpy untuk analisis data 📊
- Matplotlib & Seaborn untuk visualisasi 📈

---

3. Jalankan notebook dengan Jupyter:
   ```bash
   jupyter notebook
   ```

4. Ikuti instruksi pada `Notebook1` dan `Notebook2` untuk pelatihan serta prediksi.

---
