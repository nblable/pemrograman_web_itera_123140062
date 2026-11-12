# Praktikum Pemrograman Web - Pertemuan 5
## Python Object-Oriented Programming (OOP)

### Identitas Mahasiswa
- Nama Lengkap: Nabila Ramadhani Mujahidin
- NIM: 123140062
- Kelas Praktikum: RA

### Deskripsi Program
Program ini merupakan implementasi konsep Object-Oriented Programming (OOP) dengan Python.
Terdapat dua bagian:

1. Folder `latihan/` berisi contoh hands-on dari materi praktikum (class, object,
   inheritance, encapsulation, polymorphism, dan abstract class).
2. Folder `tugas_perpustakaan/` berisi sistem manajemen perpustakaan sederhana.

Penerapan 4 pilar OOP pada tugas perpustakaan:
- Class & Object: LibraryItem, Book, Magazine, Member, Library.
- Inheritance: Book dan Magazine mewarisi LibraryItem.
- Encapsulation: atribut protected (`_`) dan private (`__`) dengan name mangling,
  serta akses melalui property getter/setter.
- Polymorphism: method `get_detail()` dan `hitung_denda()` dioverride pada setiap
  subclass, serta dipanggil secara polimorfik pada koleksi heterogen.
- Abstraction: LibraryItem merupakan abstract class dengan abstract method.

### Struktur Berkas
```
Nabila_123140062_pertemuan5/
|-- latihan/
|   |-- 01_everything_is_object.py
|   |-- 01_procedural_vs_oop.py
|   |-- 02_class_object.py
|   |-- 03_inheritance.py
|   |-- 04_encapsulation.py
|   |-- 05_polymorphism.py
|   `-- 06_abstract_class.py
|-- tugas_perpustakaan/
|   |-- library_item.py
|   |-- member.py
|   |-- library.py
|   |-- main.py
|   `-- output.txt
|-- README.md
`-- .gitignore
```

### Panduan Menjalankan Program
Jalankan latihan:
```
cd latihan
python 02_class_object.py
```

Jalankan tugas perpustakaan:
```
cd tugas_perpustakaan
python main.py
```

### Screenshot Output
Tangkapan layar terminal saat program dijalankan (fitur penambahan, pencarian,
dan penampilan katalog) tersimpan pada berkas `tugas_perpustakaan/output.txt`.

Contoh output utama (`python main.py`):
```
Item 'Pemrograman Web dengan Python' berhasil ditambahkan ke perpustakaan.
Item 'Struktur Data dan Algoritma' berhasil ditambahkan ke perpustakaan.
Item 'InfoTeknologi' berhasil ditambahkan ke perpustakaan.
Item 'Sains Populer' berhasil ditambahkan ke perpustakaan.
Item dengan ID 'B001' sudah ada di koleksi.

===== KATALOG PERPUSTAKAAN ITERA =====
[B001] Pemrograman Web dengan Python (2024) - Tersedia
   Buku: Pemrograman Web dengan Python | Pengarang: Ahmad Fadhil | ISBN: 978-1234567890 | Halaman: 320 | Tahun: 2024
[B002] Struktur Data dan Algoritma (2023) - Tersedia
   Buku: Struktur Data dan Algoritma | Pengarang: Siti Rahma | ISBN: 978-0987654321 | Halaman: 450 | Tahun: 2023
[M001] InfoTeknologi (2025) - Tersedia
   Majalah: InfoTeknologi | Edisi: Edisi 12 | Penerbit: ITERA Press | Tahun: 2025
[M002] Sains Populer (2024) - Tersedia
   Majalah: Sains Populer | Edisi: Edisi 5 | Penerbit: Sains Indonesia | Tahun: 2024

Total item di perpustakaan: 4

--- Pencarian Item ---
Ditemukan (by ID): Buku: Struktur Data dan Algoritma | Pengarang: Siti Rahma | ISBN: 978-0987654321 | Halaman: 450 | Tahun: 2023
Hasil pencarian judul 'python':
 - [B001] Pemrograman Web dengan Python (2024) - Tersedia

--- Peminjaman ---
Nabila Ramadhani Mujahidin berhasil meminjam: Pemrograman Web dengan Python
Item 'Pemrograman Web dengan Python' sedang dipinjam, tidak bisa dipinjam lagi.
Member[M001] Nabila Ramadhani Mujahidin (nabila@itera.ac.id) - Pinjam: 1 item
Daftar pinjam member: ['B001']

--- Item yang Tersedia ---
[B002] Struktur Data dan Algoritma (2023) - Tersedia
[M001] InfoTeknologi (2025) - Tersedia
[M002] Sains Populer (2024) - Tersedia

--- Pengembalian ---
Nabila Ramadhani Mujahidin berhasil mengembalikan: Pemrograman Web dengan Python
Member[M001] Nabila Ramadhani Mujahidin (nabila@itera.ac.id) - Pinjam: 0 item

--- Perhitungan Denda (Polymorphism) ---
Pemrograman Web dengan Python: denda 5 hari = Rp 10,000
Struktur Data dan Algoritma: denda 5 hari = Rp 10,000
InfoTeknologi: denda 5 hari = Rp 5,000
Total denda semua item (5 hari): Rp 30,000

--- Uji Property Setter ---
Validasi email: Format email tidak valid!
Email member sekarang: nabila.baru@itera.ac.id
```
