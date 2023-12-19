Penjelasan singkat:

1. **Sequence Type (List, tuple, range):**

   ```python
   data_buku = baca_data("daftarbuku.txt")
   buku_list = tampil_buku()
   ```

   Penjelasan: `data_buku` dan `buku_list` merupakan variabel yang menyimpan data dalam bentuk list.

2. **Mapping Type (Dictionary):**

   ```python
   aksi_menu = {
       1: "daftarbuku",
       2: "caridata",
       # ... (bagian lain dari aksi_menu)
   }
   ```

   Penjelasan: `aksi_menu` adalah sebuah dictionary yang melakukan pemetaan antara nomor menu dengan fungsi atau perintah yang sesuai.

3. **Variabel pada Python (Casting):**

   ```python
   self.index = 0
   ```

   Penjelasan: `self.index` adalah variabel yang digunakan untuk menyimpan nilai indeks, dan inisialisasi dengan nilai 0.

4. **Pure Functions:**

   ```python
   def bersihkan_layar():
       os.system("CLS")
   ```

   Penjelasan: `bersihkan_layar` adalah fungsi yang hanya melakukan operasi untuk membersihkan layar tanpa memiliki efek samping.

5. **Lambda Expressions:**

   ```python
   urutkan_berdasarkan_tanggal = lambda tanggal_str: tuple(map(int, tanggal_str.split('/')))
   ```

   Penjelasan: `urutkan_berdasarkan_tanggal` adalah fungsi lambda yang mengonversi format tanggal.

6. **List Comprehension:**

   ```python
   sorted_buku_list = sorted(buku_iterator._baca_data())
   ```

   Penjelasan: `sorted_buku_list` adalah list yang dibuat dengan menggunakan list comprehension untuk mengurutkan data buku.

7. **Iterator:**

   ```python
   class BukuIterator:
       def __iter__(self):
           # ...
   ```

   Penjelasan: `BukuIterator` adalah kelas iterator yang digunakan untuk mengiterasi melalui data buku.

8. **Generator:**

   ```python
   def tampil_buku_generator(file_path):
       buku_iterator = BukuIterator(file_path)
       sorted_buku_list = sorted(buku_iterator._baca_data())
       for buku in sorted_buku_list:
           yield buku
   ```

   Penjelasan: `tampil_buku_generator` adalah generator yang menghasilkan buku-buku yang diurutkan.

9. **Higher Order Function:**

   ```python
   def tampilkan_dan_kembali(fungsi):
       def pembungkus(*args, **kwargs):
           # ...
       return pembungkus
   ```

   Penjelasan: `tampilkan_dan_kembali` adalah fungsi tingkat tinggi yang menerima fungsi lain sebagai argumen dan mengembalikan fungsi baru.

10. **Built-in Higher Order Functions pada python:**

    ```python
    def proses_pilihan_menu(pilihan):
        aksi = pilih_aksi_menu(pilihan)
        if callable(aksi):
            aksi()
        else:
            globals()[aksi]()
    ```

    Penjelasan: `proses_pilihan_menu` menggunakan fungsi tingkat tinggi (`callable`) untuk memproses pilihan menu.

11. **Map:**

    ```python
    peminjam_terurut = sorted(
        peminjam_data, key=lambda peminjam: urutkan_berdasarkan_tanggal(peminjam.split(',')[2]))
    ```

    Penjelasan: `sorted` dengan argumen `key` menggunakan fungsi `urutkan_berdasarkan_tanggal` sebagai pemetaan.

12. **Filter:**

    ```python
    filtered_data = [hps for hps in peminjam_data if not (hps.startswith(nama) and judul in hps)]
    ```

    Penjelasan: List comprehension digunakan untuk menyaring data peminjam berdasarkan kondisi tertentu.

13. **Reduce:**
    Tidak ada contoh langsung dari fungsi `reduce` pada kode yang diberikan.

14. **Currying:**

    ```python
    def currying_ubah_data(data_buku):
        def ubah_data(judul, judul_baru, penulis_baru, tahun_baru):
            # ...
        return ubah_data
    ```

    Penjelasan: `currying_ubah_data` adalah fungsi currying yang menghasilkan fungsi `ubah_data`.

15. **Inner Function:**

    ```python
    def currying_ubah_data(data_buku):
        def ubah_data(judul, judul_baru, penulis_baru, tahun_baru):
            # ...
        return ubah_data
    ```

    Penjelasan: `ubah_data` adalah fungsi inner yang didefinisikan di dalam fungsi `currying_ubah_data`.

16. **Ruang Lingkup Variabel:**

    ```python
    def urutkan_berdasarkan_tanggal(tanggal_str):
        hari, bulan, tahun = map(int, tanggal_str.split('/'))
        return tahun, bulan, hari
    ```

    Penjelasan: Variabel `hari`, `bulan`, dan `tahun` di dalam fungsi memiliki ruang lingkup lokal.

17. **Closure:**

    ```python
    def currying_ubah_data(data_buku):
        def ubah_data(judul, judul_baru, penulis_baru, tahun_baru):
            nonlocal data_buku
            data_buku = [perbarui_data_buku(
                data, judul, judul_baru, penulis_baru, tahun_baru) for data in data_buku]
            tulis_data("daftarbuku.txt", data_buku)
            print("\n[Data Buku Berhasil Diubah]")
        return ubah_data
    ```

    Penjelasan: Fungsi `ubah_data` adalah closure karena memiliki akses ke variabel `data_buku` yang berada di luar ruang lingkup lokalnya.

18. **Decorations:**

    ```python
    @tampilkan_dan_kembali
    def daftarbuku():
        buku_list = tampil_buku()
        for buku in buku_list:
            print(buku)
    ```

    Penjelasan: `@tampilkan_dan_kembali` digunakan untuk mendekorasi fungsi `daftarbuku`.

    Semua kutipan kode di atas bersifat singkat dan dapat diakses untuk penjelasan lebih lanjut.
