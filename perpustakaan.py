import os
import re

# Pure Functions


def bersihkan_layar():
    os.system("CLS")


def baca_data(nama_file):
    with open(nama_file, "r") as file:
        return file.readlines()


def tulis_data(nama_file, data):
    with open(nama_file, "w") as file:
        file.writelines(data)


# Lambda Expressions
def tampilkan_menu(): return (
    print("     SELAMAT DATANG DI PROGRAM PERDIG"),
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


# Mapping Type (Dictionary)
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

# List Comprehension


def tampil_buku(): return [
    f"\n{i}. {buku}" for i, buku in enumerate(sorted(baca_data("daftarbuku.txt")), start=1)
] if os.path.exists("daftarbuku.txt") else ["\n[Data tidak tersedia]"]


def cari_buku(judul): return next(
    (hasil.split(",")
     for hasil in baca_data("daftarbuku.txt") if judul in hasil), None
)

# Iterator dan Generator


def menu():
    bersihkan_layar()
    tampilkan_menu()
    return int(input("\nMasukkan kode menu yang ingin diakses : "))

# Higher Order Function


def pilih_aksi_menu(pilihan):
    return aksi_menu.get(pilihan, lambda: print("\n[Kode yang anda masukkan tidak valid!]"))

# Built-in Higher Order Functions


def proses_pilihan_menu(pilihan):
    aksi = pilih_aksi_menu(pilihan)
    if callable(aksi):
        aksi()
    else:
        globals()[aksi]()

# Inner Function


def perbarui_data_buku(data_buku, judul, judul_baru, penulis_baru, tahun_baru):
    return ",".join([judul_baru, penulis_baru, tahun_baru + "\n"]) if data_buku.startswith(judul) else data_buku

# Closure


def urutkan_berdasarkan_tanggal(tanggal_str):
    hari, bulan, tahun = map(int, tanggal_str.split('/'))
    return tahun, bulan, hari

# Decorators


def tampilkan_dan_kembali(fungsi):
    def pembungkus(*args, **kwargs):
        hasil = fungsi(*args, **kwargs)
        print("\nTekan [ENTER] untuk kembali ke menu")
        input()
        menu()
        return hasil
    return pembungkus

# Applying Decorators


@tampilkan_dan_kembali
def daftarbuku():
    buku_list = tampil_buku()
    for buku in buku_list:
        print(buku)


@tampilkan_dan_kembali
def caridata():
    judul = input("Masukkan judul buku yang ingin dicari : ")
    hasil = cari_buku(judul)

    if hasil:
        print(f"\nJudul Buku           : {hasil[0]}")
        print(f"Penulis             : {hasil[1]}")
        print(f"Tahun Terbit        : {hasil[2]}")
    else:
        print("\n[Data tidak ditemukan]")


@tampilkan_dan_kembali
def tambahdata():
    judul = input("Judul Buku    : ")
    penulis = input("Penulis Buku  : ")
    tahun = input("Tahun Terbit  : ")
    data_buku = baca_data("daftarbuku.txt")
    data_buku.append(f"{judul},{penulis},{tahun}\n")
    tulis_data("daftarbuku.txt", data_buku)
    print("\n[Data Buku Berhasil Ditambahkan]")


def input_baru():
    return input("Masukkan judul buku yang ingin diperbarui : "), input("Judul Buku    : "), input("Penulis Buku  : "), input("Tahun Terbit  : ")

# Inner Function


@tampilkan_dan_kembali
def ubahdata():
    baru = input("Masukkan judul buku yang ingin diperbarui : ")
    judul, judul_baru, penulis_baru, tahun_baru = input_baru()
    data_buku = baca_data("daftarbuku.txt")
    data_buku = [perbarui_data_buku(
        data_buku, judul, judul_baru, penulis_baru, tahun_baru) for data_buku in data_buku]
    tulis_data("daftarbuku.txt", data_buku)
    print("\n[Data Buku Berhasil Diubah]")


@tampilkan_dan_kembali
def hapusdata():
    str = input("Masukkan judul buku yang ingin dihapus : ")
    data_buku = baca_data("daftarbuku.txt")
    output = [hps for hps in data_buku if not hps.startswith(str)]
    tulis_data("daftarbuku.txt", output)
    print("\n[Data Buku Telah Terhapus]")


@tampilkan_dan_kembali
def daftarpeminjam():
    peminjam_data = baca_data("daftarpeminjam.txt")
    peminjam_terurut = sorted(
        peminjam_data, key=lambda peminjam: urutkan_berdasarkan_tanggal(peminjam.split(',')[2]))
    peminjam_list = [f"\n{i}. {peminjam}" for i, peminjam in enumerate(
        peminjam_terurut, start=1)] if peminjam_terurut else ["\n[Data tidak tersedia]"]
    for peminjam in peminjam_list:
        print(peminjam)


@tampilkan_dan_kembali
def tambahpeminjam():
    peminjam_data = baca_data("daftarpeminjam.txt")

    # Dapatkan informasi peminjam
    nama = input("Nama            : ")
    judul = input("Judul Buku       : ")

    # Periksa apakah buku ada dalam daftar buku yang tersedia
    data_buku = baca_data("daftarbuku.txt")
    if not any(judul in buku for buku in data_buku):
        print("\n[Buku tidak ditemukan. Pastikan judul buku sudah benar.]")
        return

    # Validasi dan dapatkan tanggal yang diformat dengan benar
    tanggal = input("Tanggal Peminjaman (format: dd/mm/yyyy): ")
    while not re.match(r'\d{2}/\d{2}/\d{4}', tanggal):
        print("\n[Format tanggal tidak valid. Gunakan format dd/mm/yyyy.]")
        tanggal = input("Tanggal Peminjaman (format: dd/mm/yyyy): ")

    # Tambahkan informasi peminjam ke daftar
    peminjam_data.append(f"{nama},{judul},{tanggal}\n")
    tulis_data("daftarpeminjam.txt", peminjam_data)

    print("\n[Data Peminjam Berhasil Ditambahkan]")


@tampilkan_dan_kembali
def hapuspeminjam():
    str = input("Masukkan Nama Peminjam yang Ingin Dihapus : ")
    peminjam_data = baca_data("daftarpeminjam.txt")
    output = [hps for hps in peminjam_data if not hps.startswith(str)]
    tulis_data("daftarpeminjam.txt", output)
    print("\n[Data Peminjam Telah Terhapus]")


# Program Utama
if __name__ == "__main__":
    while True:
        pilihan = menu()
        if pilihan == 9:
            break  # Keluar dari loop ketika pengguna memilih keluar
        proses_pilihan_menu(pilihan)
