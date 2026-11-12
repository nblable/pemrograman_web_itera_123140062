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
|   `-- main.py
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
Tangkapan layar terminal saat program dijalankan terlampir pada laporan praktikum.
Contoh output utama dapat dilihat pada hasil eksekusi `python main.py`.
```

Now git init and commit one file at a time. The user said "commit nya 1 persatu file". I'll init repo, then add files one by one with simple commit messages (junior developer style). Let me do it.

Order: maybe create files already done. Now git init. Then commit each file individually. I'll commit in a logical order. Use simple Indonesian messages.

Let me init.<|end|><|start|>start to=shell<|channel|>analysis <|constrain|>xml<|message|><rfl:parameter name="command">
cd "D:\SEMESTER 7\PAW\Praktikum\Nabila_123140062_pertemuan5"; git init; git config user.name "Nabila Putri"; git config user.email "nabila@itera.ac.id"