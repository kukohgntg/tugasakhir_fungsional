**Import Statements:**
1. Mengimpor modul os untuk berinteraksi dengan sistem operasi (misalnya, membersihkan layar konsol).
2. Mengimpor modul re untuk ekspresi regular
```
import os
import re
```
**Pure Functions (Fungsi Murni):**
1. bersihkan_layar(): Membersihkan layar konsol.
```
def bersihkan_layar():
    os.system("CLS")    
```
2. baca_data(nama_file): Membaca data dari file dan mengembalikannya sebagai daftar baris.
```
def baca_data(nama_file):
    with open(nama_file, "r") as file:
        return file.readlines()
```
3. tulis_data(nama_file, data): Menulis data ke dalam file.

```
def tulis_data(nama_file, data):
    with open(nama_file, "w") as file:
        file.writelines(data)
```
**Lambda Expressions (Ekspresi Lambda):**
1. tampilkan_menu(): Mengembalikan tuple dari cetakan pesan menu ke layar.
```
def tampilkan_menu():
    return (
        print(" SELAMAT DATANG DI PROGRAM PERPUSTAKAAN"),
        print("\nPilih daftar menu untuk mengakses program :\n"),
        print("[1] Lihat Daftar Buku"),
        print("[2] Cari Buku"),
        print("[3] Tambah Data Buku"),
        print("[4] Ubah Data Buku"),
        print("[5] Hapus Data Buku"),
        print("[6] Lihat Daftar Peminjam Buku"),
        print("[7] Tambah Peminjam Buku"),
        print("[8] Hapus Data Peminjam Buku"),
        print("[9] Keluar"),
    )
```
**Mapping Type (Dictionary):**
1. aksi_menu: Sebuah kamus yang memetakan opsi menu ke fungsi atau aksi yang sesuai.
```
aksi_menu = {
    1: "daftarbuku",
    2: "caridata",
    3: "tambahdata",
    4: "ubahdata",
    5: "hapusdata",
    6: "daftarpeminjam",
    7: "tambahpeminjam",
    8: "hapuspeminjam",
    9: lambda: print("\n[Anda telah keluar dari program]"),
}
```
**List Comprehension (Pemahaman List):**
1. tampil_buku(): Membaca file "daftarbuku.txt", mengurutkan isinya, dan mengembalikan daftar buku yang diformat.
```
def tampil_buku():
    return [
        f"\n{i}. {buku}" for i, buku in enumerate(sorted(baca_data("daftarbuku.txt")), start=1)
    ] if os.path.exists("daftarbuku.txt") else ["\n[Data tidak tersedia]"]
``` 
**Iterator dan Generator:**
1. Tidak ada penggunaan iterator atau generator yang eksplisit dalam kode ini.
```
def cari_buku(judul):
    return next(
        (hasil.split(",") for hasil in baca_data("daftarbuku.txt") if judul in hasil), None
    )
```
**Higher Order Function (Fungsi Orde Tinggi):**
1. menu(): Membersihkan layar, menampilkan menu, dan mengambil input pengguna untuk pemilihan menu.
```
def menu():
    bersihkan_layar()
    tampilkan_menu()
    return int(input("\nMasukkan kode menu yang ingin diakses : "))
```
**Built-in Higher Order Functions (Fungsi Bawaan Orde Tinggi):**
1. proses_pilihan_menu(pilihan): Mengambil pilihan menu, mencari aksi yang sesuai, dan menjalankannya.
```
def pilih_aksi_menu(pilihan):
    return aksi_menu.get(pilihan, lambda: print("\n[Kode yang anda masukkan tidak valid!]"))
```
**Inner Function (Fungsi Dalam):**
1. perbarui_data_buku(data_buku, judul, judul_baru, penulis_baru, tahun_baru): Sebuah fungsi dalam yang digunakan untuk memperbarui data buku.
```
def proses_pilihan_menu(pilihan):
    aksi = pilih_aksi_menu(pilihan)
    if callable(aksi):
        aksi()
    else:
        globals()[aksi]()
```
**Closure**
1. urutkan_berdasarkan_tanggal(tanggal_str): Sebuah closure yang mengonversi string tanggal menjadi tuple untuk tujuan pengurutan.
```
def urutkan_berdasarkan_tanggal(tanggal_str):
    hari, bulan, tahun = map(int, tanggal_str.split('/'))
    return tahun, bulan, hari
```
**Decorators (Dekorator):**
1. tampilkan_dan_kembali(fungsi): Sebuah dekorator yang membungkus fungsi, mencetak pesan, menunggu input pengguna, dan kembali ke menu utama.
```
def tampilkan_dan_kembali(fungsi):
    def pembungkus(*args, **kwargs):
        hasil = fungsi(*args, **kwargs)
        print("\nTekan [ENTER] untuk kembali ke menu")
        input()
        menu()
        return hasil
    return pembungkus
```
**Applying Decorators (Penerapan Dekorator):**
1. Dekorator diterapkan pada beberapa fungsi seperti daftarbuku(), caridata(), dll.
```
@tampilkan_dan_kembali
def daftarbuku():
    buku_list = tampil_buku()
    for buku in buku_list:
        print(buku)
```
**Main Program:**
1. Sebuah loop tak terbatas yang secara berulang menampilkan menu, mengambil input pengguna, dan menjalankan aksi yang sesuai sampai pengguna memilih untuk keluar.
```
if __name__ == "__main__":
    while True:
        pilihan = menu()
        if pilihan == 9:
            break  # Keluar dari loop ketika pengguna memilih keluar
        proses_pilihan_menu(pilihan)
```