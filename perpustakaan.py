import os

# Pure Functions


def clear_screen():
    os.system("CLS")


def read_books_data():
    with open("daftarbuku.txt", "r") as bukadata:
        return bukadata.readlines()


def write_books_data(data):
    with open("daftarbuku.txt", "w") as bukadata:
        bukadata.writelines(data)


def read_peminjam_data():
    with open("daftarpeminjam.txt", "r") as bukadata:
        return bukadata.readlines()


def write_peminjam_data(data):
    with open("daftarpeminjam.txt", "w") as bukadata:
        bukadata.writelines(data)


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

# List Comprehension


def display_books():
    books_data = read_books_data()
    sorted_books = sorted(books_data)
    return [f"\n{i}. {book}" for i, book in enumerate(sorted_books, start=1)] if sorted_books else ["\n[Data tidak tersedia]"]


def search_book(title):
    books_data = read_books_data()
    results = [book for book in books_data if title in book]

    if results:
        result = results[0].split(",")
        return result
    else:
        return None

# Iterator dan Generator


def menu():
    clear_screen()
    print_menu()
    return int(input("\nMasukkan kode menu yang ingin diakses : "))

# Higher Order Function


def select_menu_action(choice):
    menu_actions = {
        1: daftarbuku,
        2: caridata,
        3: tambahdata,
        4: ubahdata,
        5: hapusdata,
        6: daftarpeminjam,
        7: tambahpeminjam,
        8: hapuspeminjam,
        9: lambda: print("\n[Anda telah keluar dari program]"),
    }
    return menu_actions.get(choice, lambda: print("\n[Kode yang anda masukkan tidak valid!]"))

# Built-in Higher Order Functions


def process_menu_choice(choice):
    action = select_menu_action(choice)
    action()

# Currying


def input_with_message(message):
    return input(message)


def input_title(): return input_with_message(
    "Masukkan judul buku yang ingin dicari : ")


def input_data(message): return input_with_message(message)


def tambah_data():
    judul = input_data("Judul Buku    : ")
    penulis = input_data("Penulis Buku  : ")
    tahun = input_data("Tahun Terbit  : ")
    bukadata = read_books_data()
    bukadata.append(f"{judul},{penulis},{tahun}\n")
    write_books_data(bukadata)
    print("\n[Data Buku Berhasil Ditambahkan]")


def input_baru():
    return input_title(), input_data("Masukkan data baru\nJudul Buku    : "), input_data("Penulis Buku  : "), input_data("Tahun Terbit  : ")

# Inner Function


def ubah_data():
    def update_book_data(data_buku, title, judulbr, penulisbr, tahunbr):
        return ",".join([judulbr, penulisbr, tahunbr + "\n"]) if data_buku.startswith(title) else data_buku

    baru = input_title()
    title, judulbr, penulisbr, tahunbr = input_baru()
    bukadata = read_books_data()
    bukadata = [update_book_data(
        data_buku, title, judulbr, penulisbr, tahunbr) for data_buku in bukadata]
    write_books_data(bukadata)
    print("\n[Data Buku Berhasil Diubah]")


def hapus_data():
    str = input_title()
    bukadata = read_books_data()
    output = [hps for hps in bukadata if not hps.startswith(str)]
    write_books_data(output)
    print("\n[Data Buku Telah Terhapus]")

# Closure


def display_peminjam():
    peminjam_data = read_peminjam_data()
    sorted_peminjam = sorted(peminjam_data)
    return [f"\n{i}. {peminjam}" for i, peminjam in enumerate(sorted_peminjam, start=1)] if sorted_peminjam else ["\n[Data tidak tersedia]"]


def tambah_peminjam():
    peminjam_data = read_peminjam_data()

    # Get borrower information
    nama = input_data("Nama            : ")
    judul = input_data("Judul Buku       : ")

    # Check if the book exists in the list of available books
    books_data = read_books_data()
    if not any(judul in book for book in books_data):
        print("\n[Buku tidak ditemukan. Pastikan judul buku sudah benar.]")
        return

    tanggal = input_data("Tanggal Peminjaman : ")

    # Add borrower information to the list
    peminjam_data.append(f"{nama},{judul},{tanggal}\n")
    write_peminjam_data(peminjam_data)

    print("\n[Data Peminjam Berhasil Ditambahkan]")


def hapus_peminjam():
    str = input_data("Masukkan Nama Peminjam yang Ingin Dihapus : ")
    peminjam_data = read_peminjam_data()
    output = [hps for hps in peminjam_data if not hps.startswith(str)]
    write_peminjam_data(output)
    print("\n[Data Peminjam Telah Terhapus]")

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
    title = input_title()
    result = search_book(title)

    if result:
        print(f"\nJudul Buku           : {result[0]}")
        print(f"Penulis             : {result[1]}")
        print(f"Tahun Terbit        : {result[2]}")
    else:
        print("\n[Data tidak ditemukan]")


@display_and_return
def tambahdata():
    tambah_data()
    tmbhdata = input_data("\nIngin menambahkan buku lagi? (Ya/Tidak) : ")
    if tmbhdata.lower() == "ya":
        tambahdata()


@display_and_return
def ubahdata():
    ubah_data()
    ubhdata = input_data("\nIngin mengubah data buku lagi? (Ya/Tidak) : ")
    if ubhdata.lower() == "ya":
        ubahdata()


@display_and_return
def hapusdata():
    hapus_data()
    hpsdata = input_data("\nIngin menghapus data buku lagi? (Ya/Tidak) : ")
    if hpsdata.lower() == "ya":
        hapusdata()


@display_and_return
def daftarpeminjam():
    peminjam_list = display_peminjam()
    for peminjam in peminjam_list:
        print(peminjam)


@display_and_return
def tambahpeminjam():
    tambah_peminjam()
    tmbhpeminjam = input_data(
        "\nIngin menambahkan data peminjam lagi? (Ya/Tidak) : ")
    if tmbhpeminjam.lower() == "ya":
        tambahpeminjam()


@display_and_return
def hapuspeminjam():
    hapus_peminjam()
    hpspeminjam = input_data(
        "\nIngin menghapus data peminjam lagi? (Ya/Tidak) : ")
    if hpspeminjam.lower() == "ya":
        hapuspeminjam()


# Main Program
if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == 9:
            break  # Exit the loop when the user chooses to exit
        process_menu_choice(choice)
