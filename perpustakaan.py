import os
import re

# Pure Functions


def clear_screen():
    os.system("CLS")


def read_data(file_name):
    with open(file_name, "r") as file:
        return file.readlines()


def write_data(file_name, data):
    with open(file_name, "w") as file:
        file.writelines(data)


# Lambda Expressions
def print_menu(): return (
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
menu_actions = {
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


def display_books(): return [
    f"\n{i}. {book}" for i, book in enumerate(sorted(read_data("daftarbuku.txt")), start=1)
] if os.path.exists("daftarbuku.txt") else ["\n[Data tidak tersedia]"]


def search_book(title): return next(
    (result.split(",")
     for result in read_data("daftarbuku.txt") if title in result), None
)

# Iterator dan Generator


def menu():
    clear_screen()
    print_menu()
    return int(input("\nMasukkan kode menu yang ingin diakses : "))

# Higher Order Function


def select_menu_action(choice):
    return menu_actions.get(choice, lambda: print("\n[Kode yang anda masukkan tidak valid!]"))

# Built-in Higher Order Functions


def process_menu_choice(choice):
    action = select_menu_action(choice)
    if callable(action):
        action()
    else:
        globals()[action]()

# Inner Function


def update_book_data(data_buku, title, judulbr, penulisbr, tahunbr):
    return ",".join([judulbr, penulisbr, tahunbr + "\n"]) if data_buku.startswith(title) else data_buku

# Closure


def sort_by_date(date_str):
    day, month, year = map(int, date_str.split('/'))
    return year, month, day

# Decorators


def display_and_return(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("\nTekan [ENTER] untuk kembali ke menu")
        input()
        menu()
        return result
    return wrapper

# Applying Decorators


@display_and_return
def daftarbuku():
    books_list = display_books()
    for book in books_list:
        print(book)


@display_and_return
def caridata():
    title = input("Masukkan judul buku yang ingin dicari : ")
    result = search_book(title)

    if result:
        print(f"\nJudul Buku           : {result[0]}")
        print(f"Penulis             : {result[1]}")
        print(f"Tahun Terbit        : {result[2]}")
    else:
        print("\n[Data tidak ditemukan]")


@display_and_return
def tambahdata():
    judul = input("Judul Buku    : ")
    penulis = input("Penulis Buku  : ")
    tahun = input("Tahun Terbit  : ")
    bukadata = read_data("daftarbuku.txt")
    bukadata.append(f"{judul},{penulis},{tahun}\n")
    write_data("daftarbuku.txt", bukadata)
    print("\n[Data Buku Berhasil Ditambahkan]")


def input_baru():
    return input("Masukkan judul buku yang ingin diperbarui : "), input("Judul Buku    : "), input("Penulis Buku  : "), input("Tahun Terbit  : ")

# Inner Function


@display_and_return
def ubahdata():
    baru = input("Masukkan judul buku yang ingin diperbarui : ")
    title, judulbr, penulisbr, tahunbr = input_baru()
    bukadata = read_data("daftarbuku.txt")
    bukadata = [update_book_data(
        data_buku, title, judulbr, penulisbr, tahunbr) for data_buku in bukadata]
    write_data("daftarbuku.txt", bukadata)
    print("\n[Data Buku Berhasil Diubah]")


@display_and_return
def hapusdata():
    str = input("Masukkan judul buku yang ingin dihapus : ")
    bukadata = read_data("daftarbuku.txt")
    output = [hps for hps in bukadata if not hps.startswith(str)]
    write_data("daftarbuku.txt", output)
    print("\n[Data Buku Telah Terhapus]")


@display_and_return
def daftarpeminjam():
    peminjam_data = read_data("daftarpeminjam.txt")
    sorted_peminjam = sorted(
        peminjam_data, key=lambda peminjam: sort_by_date(peminjam.split(',')[2]))
    peminjam_list = [f"\n{i}. {peminjam}" for i, peminjam in enumerate(
        sorted_peminjam, start=1)] if sorted_peminjam else ["\n[Data tidak tersedia]"]
    for peminjam in peminjam_list:
        print(peminjam)


@display_and_return
def tambahpeminjam():
    peminjam_data = read_data("daftarpeminjam.txt")

    # Get borrower information
    nama = input("Nama            : ")
    judul = input("Judul Buku       : ")

    # Check if the book exists in the list of available books
    books_data = read_data("daftarbuku.txt")
    if not any(judul in book for book in books_data):
        print("\n[Buku tidak ditemukan. Pastikan judul buku sudah benar.]")
        return

    # Validate and get a properly formatted date
    tanggal = input("Tanggal Peminjaman (format: dd/mm/yyyy): ")
    while not re.match(r'\d{2}/\d{2}/\d{4}', tanggal):
        print("\n[Format tanggal tidak valid. Gunakan format dd/mm/yyyy.]")
        tanggal = input("Tanggal Peminjaman (format: dd/mm/yyyy): ")

    # Add borrower information to the list
    peminjam_data.append(f"{nama},{judul},{tanggal}\n")
    write_data("daftarpeminjam.txt", peminjam_data)

    print("\n[Data Peminjam Berhasil Ditambahkan]")


@display_and_return
def hapuspeminjam():
    str = input("Masukkan Nama Peminjam yang Ingin Dihapus : ")
    peminjam_data = read_data("daftarpeminjam.txt")
    output = [hps for hps in peminjam_data if not hps.startswith(str)]
    write_data("daftarpeminjam.txt", output)
    print("\n[Data Peminjam Telah Terhapus]")


# Main Program
if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == 9:
            break  # Exit the loop when the user chooses to exit
        process_menu_choice(choice)
