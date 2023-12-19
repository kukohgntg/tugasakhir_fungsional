# List Comprehension

```
def tampil_buku(): return [
    f"\n{i}. {buku}" for i, buku in enumerate(sorted(baca_data("daftarbuku.txt")), start=1)
] if os.path.exists("daftarbuku.txt") else ["\n[Data tidak tersedia]"]

```

Penjelasan: List comprehension digunakan untuk membuat list yang berisi informasi buku. enumerate digunakan untuk mendapatkan indeks dan nilai dalam list.

# Mapping Type (Dictionary)

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

Penjelasan: aksi_menu adalah sebuah dictionary yang memetakan angka ke aksi yang sesuai dalam program.

# Variabel pada Python (Casting)

```
hari, bulan, tahun = map(int, tanggal_str.split('/'))

```

Penjelasan: Menggunakan fungsi map untuk mengonversi string yang didapatkan dari input tanggal ke tipe data integer.

# Pure Functions

```
def bersihkan_layar():
    os.system("CLS")

def baca_data(nama_file):
    with open(nama_file, "r") as file:
        return file.readlines()

def tulis_data(nama_file, data):
    with open(nama_file, "w") as file:
        file.writelines(data)

```

Penjelasan: Fungsi-fungsi ini adalah pure functions karena tidak memiliki efek samping dan mengembalikan nilai berdasarkan input.

# Lambda Expressions

```
def tampilkan_menu(): return (
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

Penjelasan: Menggunakan lambda expression untuk mendefinisikan fungsi yang mereturn menu tampilan.

# List Comprehension

```
def tampil_buku(): return [
    f"\n{i}. {buku}" for i, buku in enumerate(sorted(baca_data("daftarbuku.txt")), start=1)
] if os.path.exists("daftarbuku.txt") else ["\n[Data tidak tersedia]"]

```

Penjelasan: Menggunakan list comprehension untuk membuat list yang berisi informasi buku.

# Iterator Class

```
class BukuIterator:
    # ...

```

Penjelasan: Membuat kelas iterator BukuIterator untuk mengiterasi data buku.

# Generator

```
def tampil_buku_generator(file_path):
    buku_iterator = BukuIterator(file_path)
    sorted_buku_list = sorted(buku_iterator._baca_data())
    for buku in sorted_buku_list:
        yield buku

```

Penjelasan: Menggunakan generator function tampil_buku_generator untuk menghasilkan nilai satu per satu dari buku.

# Higher Order Function

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

Penjelasan: tampilkan_dan_kembali adalah higher order function karena menerima fungsi sebagai argumen dan mengembalikan fungsi lain.

# Built-in Higher Order Functions pada python

```
def proses_pilihan_menu(pilihan):
    aksi = pilih_aksi_menu(pilihan)
    if callable(aksi):
        aksi()
    else:
        globals()[aksi]()

```

Penjelasan: Menggunakan fungsi callable untuk memeriksa apakah sebuah objek dapat dipanggil dan globals() untuk memanggil fungsi dengan nama yang dinamis.

# Map

```
hari, bulan, tahun = map(int, tanggal_str.split('/'))

```

Penjelasan: Menggunakan fungsi map untuk mengonversi string menjadi integer pada pemisahan tanggal.

# Filter data yang sesuai dengan nama dan judul buku

```
filtered_data = [hps for hps in peminjam_data if not (hps.startswith(nama) and judul in hps)]

```

Penjelasan: Menggunakan list comprehension untuk menyaring data peminjam berdasarkan nama dan judul buku.

# Currying Function

```
def currying_ubah_data(data_buku):
    def ubah_data(judul, judul_baru, penulis_baru, tahun_baru):
        nonlocal data_buku
        data_buku = [perbarui_data_buku(
            data, judul, judul_baru, penulis_baru, tahun_baru) for data in data_buku]
        tulis_data("daftarbuku.txt", data_buku)
        print("\n[Data Buku Berhasil Diubah]")

    return ubah_data

```

Penjelasan: currying_ubah_data adalah sebuah fungsi yang mengembalikan fungsi lain (ubah_data). Currying memungkinkan penggunaan sebagian argumen dan memberikan fungsi yang baru yang mengharapkan sisa argumen.

# Inner Function

```
def perbarui_data_buku(data_buku, judul, judul_baru, penulis_baru, tahun_baru):
    return ",".join([judul_baru, penulis_baru, tahun_baru + "\n"]) if data_buku.startswith(judul) else data_buku

```

Penjelasan: perbarui_data_buku adalah fungsi dalam fungsi lain (ubah_data).

# Closure

```
def urutkan_berdasarkan_tanggal(tanggal_str):
    hari, bulan, tahun = map(int, tanggal_str.split('/'))
    return tahun, bulan, hari

```

Penjelasan: Fungsi urutkan_berdasarkan_tanggal adalah contoh dari closure karena menggunakan variabel dari lingkup luar (tanggal_str).

# Decorators

```
@tampilkan_dan_kembali
def daftarbuku():
    # ...

```

Penjelasan: Menggunakan decorator tampilkan_dan_kembali untuk mengubah perilaku fungsi daftarbuku.
