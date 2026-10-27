# Praktik: Pengelolaan Data Mahasiswa dengan Dictionary

mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "3A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "3A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "3B", "nilai": 90},
    "A004": {"nama": "Dina", "kelas": "3B", "nilai": 88},
    "A005": {"nama": "Eko", "kelas": "3A", "nilai": 80}
}


# Fungsi untuk mencari data mahasiswa
def cari_mahasiswa(nim):
    if nim in mahasiswa:
        return mahasiswa[nim]
    else:
        return "Data tidak ditemukan"


# Fungsi untuk menghitung rata-rata nilai
def hitung_rata_rata():
    total = 0

    for data in mahasiswa.values():
        total += data["nilai"]

    return total / len(mahasiswa)


# Menampilkan data berdasarkan NIM
print("=== PENCARIAN DATA MAHASISWA ===")
print("A003:", cari_mahasiswa("A003"))
print("A999:", cari_mahasiswa("A999"))

# Mengubah nilai mahasiswa A002
mahasiswa["A002"]["nilai"] = 82
print("\nNilai A002 setelah diubah:", mahasiswa["A002"]["nilai"])

# Menambahkan mahasiswa baru
mahasiswa["A006"] = {
    "nama": "Fani",
    "kelas": "3B",
    "nilai": 86
}

# Menampilkan seluruh data menggunakan items()
print("\n=== SELURUH DATA MAHASISWA ===")
for nim, data in mahasiswa.items():
    print(nim, ":", data)

# Menghitung rata-rata nilai
print("\nRata-rata nilai mahasiswa:", hitung_rata_rata())