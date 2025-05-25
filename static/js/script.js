// Menunggu hingga seluruh halaman HTML dimuat sebelum menjalankan skrip
document.addEventListener('DOMContentLoaded', function() {
    
    // Ambil elemen-elemen yang kita butuhkan dari halaman
    const testModeToggle = document.getElementById('test-mode-toggle');
    const testButtons = document.getElementById('test-buttons-wrapper');

    // Tambahkan 'event listener' untuk mendeteksi perubahan pada saklar
    testModeToggle.addEventListener('change', function() {
        // 'this.checked' akan bernilai 'true' jika saklar aktif, dan 'false' jika tidak
        if (this.checked) {
            // Jika saklar aktif, tampilkan tombol-tombol ujicoba
            testButtons.style.display = 'flex';
        } else {
            // Jika saklar nonaktif, sembunyikan tombol-tombol ujicoba
            testButtons.style.display = 'none';
        }
    });

});


function fillFormNegative() {
    // Contoh data untuk pasien yang kemungkinan besar TIDAK diabetes (Outcome = 0)
    document.getElementById('pregnancies').value = 1;
    document.getElementById('glucose').value = 89;
    document.getElementById('blood_pressure').value = 66;
    document.getElementById('skin_thickness').value = 23;
    document.getElementById('insulin').value = 94;
    document.getElementById('bmi').value = 28.1;
    document.getElementById('dpf').value = 0.167;
    document.getElementById('age').value = 21;
}

function fillFormPositive() {
    // Contoh data untuk pasien yang kemungkinan besar IYA diabetes (Outcome = 1)
    document.getElementById('pregnancies').value = 6;
    document.getElementById('glucose').value = 148;
    document.getElementById('blood_pressure').value = 72;
    document.getElementById('skin_thickness').value = 35;
    document.getElementById('insulin').value = 125; // Menggunakan nilai median insulin agar lebih realistis
    document.getElementById('bmi').value = 33.6;
    document.getElementById('dpf').value = 0.627;
    document.getElementById('age').value = 50;
}