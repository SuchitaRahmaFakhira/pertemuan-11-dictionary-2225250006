Pertemuan 11 - Dictionary/Map

Nama: Suchita Rahma Fakhira
NIM: 2225250006
Kelas: 3B

Tujuan

Memahami penggunaan dictionary untuk mengelola data mahasiswa, mulai dari pencarian, penambahan, pembaruan, hingga perhitungan rata-rata nilai.

Struktur Data

Program menggunakan dictionary "data_mahasiswa" dengan NIM sebagai key utama. Setiap value berupa dictionary yang berisi nama, kelas, dan nilai mahasiswa. Program menggunakan fungsi "cari_mahasiswa()" untuk mencari data berdasarkan NIM dan "rata_rata_nilai()" untuk menghitung rata-rata nilai mahasiswa.

Cara Menjalankan

python praktik/data_mahasiswa.py

Test Case

Kasus| Hasil yang diharapkan| Hasil aktual| Status
Pencarian A003| Data Citra ditampilkan| Data Citra ditemukan| Berhasil
Pencarian A999| Pesan Data tidak ditemukan| Data tidak ditemukan| Berhasil
Pembaruan nilai A002| Nilai berubah menjadi 82| Nilai A002 menjadi 82| Berhasil
Penambahan A006| Key A006 tersedia| Data A006 berhasil ditambahkan| Berhasil
Rekap menggunakan "items()"| Semua NIM dan data tampil| A001–A006 ditampilkan| Berhasil
Rata-rata nilai| Rata-rata dihitung dengan benar| 83.50| Berhasil

Refleksi

Kesulitan yang mungkin terjadi dalam penggunaan dictionary adalah mengakses data yang belum tersedia sehingga program mengalami error. Untuk mengatasinya, dapat digunakan pengecekan key atau metode get() agar program dapat menangani data yang tidak ditemukan dengan baik.
