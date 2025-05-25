# Aplikasi Prediksi Diabetes Gestasional Berbasis Web

Aplikasi web sederhana yang ditenagai oleh model Machine Learning untuk memprediksi risiko diabetes gestasional pada wanita berdasarkan beberapa atribut diagnostik. Proyek ini dibangun menggunakan Python dengan framework Flask untuk backend dan model klasifikasi XGBoost untuk prediksinya.

## ✨ Fitur-Fitur

- **Antarmuka Web Interaktif**: Form input yang mudah digunakan untuk memasukkan data pasien.
- **Prediksi Berbasis AI**: Menggunakan model klasifikasi *eXtreme Gradient Boosting (XGBoost)* yang telah dilatih untuk memberikan hasil prediksi.
- **Hasil Real-time**: Dapatkan hasil prediksi ("Berisiko Rendah" atau "Berisiko Tinggi") secara langsung setelah data dikirim.
- **Mode Ujicoba**: Dilengkapi dengan saklar (toggle switch) untuk mengaktifkan "Mode Ujicoba".
- **Pengisian Data Otomatis**: Dalam Mode Ujicoba, tersedia tombol untuk mengisi form secara otomatis dengan data contoh kasus positif dan negatif untuk mempercepat pengujian.
- **Desain Bersih & Responsif**: Tampilan yang rapi dan dapat menyesuaikan diri dengan berbagai ukuran layar.
- **Pola Desain PRG**: Menerapkan pola Post/Redirect/Get untuk pengalaman pengguna yang lebih baik (mencegah *form resubmission* saat refresh).

## 🛠️ Teknologi yang Digunakan

- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn, Pandas, NumPy, XGBoost, Joblib
- **Frontend**: HTML, CSS, JavaScript