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


<table>
  <thead>
    <tr>
      <th>Kasus</th>
      <th>Hasil yang diharapkan</th>
      <th>Hasil aktual</th>
      <th>Status</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Pencarian A003</td>
      <td>Data Citra ditampilkan</td>
      <td>Data Citra ditemukan</td>
      <td>Berhasil</td>
    </tr>
    <tr>
      <td>Pencarian A999</td>
      <td>Pesan data tidak ditemukan</td>
      <td>Data tidak ditemukan</td>
      <td>Berhasil</td>
    </tr>
    <tr>
      <td>Pembaruan nilai A002</td>
      <td>Nilai berubah menjadi 82</td>
      <td>Nilai A002 menjadi 82</td>
      <td>Berhasil</td>
    </tr>
    <tr>
      <td>Penambahan A006</td>
      <td>Key A006 tersedia</td>
      <td>Data A006 berhasil ditambahkan</td>
      <td>Berhasil</td>
    </tr>
    <tr>
      <td>Rekap menggunakan items()</td>
      <td>Semua NIM dan data tampil</td>
      <td>A001–A006 ditampilkan</td>
      <td>Berhasil</td>
    </tr>
    <tr>
      <td>Rata-rata nilai</td>
      <td>Rata-rata dihitung dengan benar</td>
      <td>83.50</td>
      <td>Berhasil</td>
    </tr>
  </tbody>
</table>


Refleksi

Kesulitan yang mungkin terjadi dalam penggunaan dictionary adalah mengakses data yang belum tersedia sehingga program mengalami error. Untuk mengatasinya, dapat digunakan pengecekan key atau metode get() agar program dapat menangani data yang tidak ditemukan dengan baik.
