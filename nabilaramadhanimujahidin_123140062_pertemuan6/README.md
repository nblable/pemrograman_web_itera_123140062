# Praktikum Pemrograman Web - Pertemuan 6

## Aplikasi CRUD Sederhana dengan Pyramid dan PostgreSQL

### Identitas Mahasiswa

- Nama Lengkap: Nabila Ramadhani Mujahidin
- NIM: 123140062
- Kelas Praktikum: RA

### Deskripsi Aplikasi

Aplikasi web RESTful API berbasis **Pyramid Framework** dan **PostgreSQL**
untuk pengelolaan data akademik. Aplikasi dikembangkan dari struktur
*cookiecutter* resmi `pyramid-cookiecutter-alchemy` dan menyediakan dua
modul CRUD lengkap:

1. **Mahasiswa** - pengelolaan data mahasiswa (NIM, nama, jurusan,
   tanggal lahir, alamat).
2. **Matakuliah** - pengelolaan data mata kuliah (kode MK, nama MK, SKS,
   semester) sebagai tugas Pertemuan 6.

Seluruh endpoint mengembalikan JSON dan menerapkan status code HTTP yang
sesuai (`200 OK`, `400 Bad Request`, `404 Not Found`). Lapisan basis data
menggunakan SQLAlchemy ORM, perubahan skema dikelola dengan Alembic, dan
transaksi diikat ke *lifecycle* request melalui `pyramid_tm` +
`zope.sqlalchemy` (commit otomatis saat sukses, rollback saat error).

### Teknologi yang Digunakan

| Komponen | Keterangan |
| --- | --- |
| Python 3.10+ | Runtime aplikasi (diuji pada Python 3.13) |
| Pyramid 2.x | Web framework dan URL dispatch |
| SQLAlchemy 2.0 | ORM dan session management |
| PostgreSQL 16 | Basis data relasional |
| Alembic | Migrasi skema database |
| Jinja2 | Template engine halaman utama |
| Waitress | WSGI server development |
| pytest + WebTest | Pengujian otomatis endpoint |

### Struktur Direktori

```
nabilaramadhanimujahidin_123140062_pertemuan6/
├── development.ini                  # Konfigurasi server & database development
├── production.ini                   # Konfigurasi deployment production
├── pytest.ini                       # Konfigurasi pytest
├── setup.py                         # Metadata dan dependensi package
├── README.md                        # Dokumentasi dan bukti pengujian
├── README.txt
├── .gitignore
├── screenshots/                     # Bukti tangkapan layar pengujian
│   ├── 01_setup_database_migrasi.png
│   ├── 02_mahasiswa_read.png
│   ├── 03_mahasiswa_write.png
│   ├── 04_matakuliah_read.png
│   ├── 05_matakuliah_write.png
│   └── 06_pytest.png
└── pyramid_mahasiswa/
    ├── __init__.py                  # Entry point WSGI (app factory)
    ├── routes.py                    # URL dispatch seluruh endpoint
    ├── tests.py                     # Pengujian otomatis CRUD
    ├── alembic/
    │   ├── env.py
    │   ├── script.py.mako
    │   └── versions/
    │       ├── 20261119_create_mahasiswa_table.py
    │       └── 20261119_create_matakuliah_table.py
    ├── models/
    │   ├── __init__.py              # Engine, session factory, registrasi model
    │   ├── meta.py                  # Declarative Base
    │   ├── mahasiswa.py             # Model ORM Mahasiswa
    │   └── matakuliah.py            # Model ORM Matakuliah
    ├── scripts/
    │   ├── __init__.py
    │   └── initialize_db.py         # Seeding data awal
    ├── static/
    ├── templates/
    └── views/
        ├── __init__.py
        ├── default.py               # Halaman utama
        ├── mahasiswa.py             # View CRUD Mahasiswa
        ├── matakuliah.py            # View CRUD Matakuliah
        └── notfound.py              # Handler kustom HTTP 404
```

### Prasyarat

- Python 3.10 atau lebih baru
- PostgreSQL 14 atau lebih baru (diuji pada PostgreSQL 16)
- `psql` dan `pip` tersedia di PATH

### Langkah Instalasi

1. Masuk ke folder proyek Pertemuan 6:

   ```bash
   cd nabilaramadhanimujahidin_123140062_pertemuan6
   ```

2. Buat dan aktifkan virtual environment:

   ```bash
   python -m venv venv

   # Windows (PowerShell)
   venv\Scripts\Activate.ps1

   # macOS / Linux
   source venv/bin/activate
   ```

   Jika PowerShell menolak aktivasi script, jalankan sekali:

   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

3. Perbarui pip lalu pasang aplikasi beserta dependensi pengujian:

   ```bash
   pip install --upgrade pip setuptools wheel
   pip install -e ".[testing]"
   pip install psycopg2-binary
   ```

4. Verifikasi instalasi:

   ```bash
   pip list
   ```

   Pastikan paket `pyramid-mahasiswa`, `pyramid`, `SQLAlchemy`, `alembic`,
   dan `psycopg2-binary` tercantum.

> Catatan: `setup.py` membatasi `SQLAlchemy >= 2.0, < 2.1` agar driver
> `postgresql://` memakai `psycopg2` (sesuai materi). Pada SQLAlchemy 2.1+
> dialek `postgresql://` secara default memilih driver `psycopg` versi 3.

### Setup Database PostgreSQL

Buka shell `psql` sebagai superuser:

```bash
psql -U postgres
```

Jalankan perintah SQL berikut:

```sql
CREATE DATABASE pyramid_mahasiswa;
CREATE USER pyramid_user WITH ENCRYPTED PASSWORD 'pyramid_pass';
GRANT ALL PRIVILEGES ON DATABASE pyramid_mahasiswa TO pyramid_user;

-- Wajib untuk PostgreSQL 15 ke atas
\c pyramid_mahasiswa
GRANT ALL ON SCHEMA public TO pyramid_user;
\q
```

Uji koneksi user aplikasi:

```bash
psql -h localhost -U pyramid_user -d pyramid_mahasiswa
# masukkan password: pyramid_pass
# prompt berubah menjadi: pyramid_mahasiswa=>
\q
```

### Konfigurasi Koneksi Database

Buka `development.ini` dan pastikan baris `sqlalchemy.url` mengarah ke
PostgreSQL:

```ini
sqlalchemy.url = postgresql://pyramid_user:pyramid_pass@localhost:5432/pyramid_mahasiswa
```

### Migrasi Database dan Seeding

Pastikan virtual environment aktif dan terminal berada di root proyek
(sejajar dengan `development.ini`).

1. Terapkan seluruh revisi migrasi:

   ```bash
   alembic -c development.ini upgrade head
   ```

2. Cek revisi yang aktif:

   ```bash
   alembic -c development.ini current
   ```

   Output yang diharapkan berakhiran `(head)`.

3. Masukkan data awal (2 mahasiswa dan 3 mata kuliah):

   ```bash
   python -m pyramid_mahasiswa.scripts.initialize_db development.ini
   ```

4. Verifikasi data langsung di PostgreSQL:

   ```bash
   psql -h localhost -U pyramid_user -d pyramid_mahasiswa \
     -c "SELECT id, nim, nama, jurusan FROM mahasiswa;"
   psql -h localhost -U pyramid_user -d pyramid_mahasiswa \
     -c "SELECT id, kode_mk, nama_mk, sks, semester FROM matakuliah;"
   ```

Skrip seeding bersifat idempotent: data tidak diduplikasi ketika perintah
dijalankan ulang.

### Menjalankan Server

```bash
pserve development.ini --reload
```

Server Waitress berjalan di `http://localhost:6543`. Halaman utama dapat
dibuka di browser, sedangkan endpoint API diuji melalui cURL/Postman.

### Daftar Endpoint API

#### Mahasiswa

| Method | URL | Fungsi | Status sukses |
| --- | --- | --- | --- |
| GET | `/api/mahasiswa` | Menampilkan seluruh mahasiswa | 200 |
| GET | `/api/mahasiswa/{id}` | Menampilkan detail mahasiswa | 200 |
| POST | `/api/mahasiswa` | Menambah mahasiswa baru | 200 |
| PUT | `/api/mahasiswa/{id}` | Memperbarui data mahasiswa | 200 |
| DELETE | `/api/mahasiswa/{id}` | Menghapus mahasiswa | 200 |

#### Matakuliah

| Method | URL | Fungsi | Status sukses |
| --- | --- | --- | --- |
| GET | `/api/matakuliah` | Menampilkan seluruh mata kuliah | 200 |
| GET | `/api/matakuliah/{id}` | Menampilkan detail mata kuliah | 200 |
| POST | `/api/matakuliah` | Menambah mata kuliah baru | 200 |
| PUT | `/api/matakuliah/{id}` | Memperbarui data mata kuliah | 200 |
| DELETE | `/api/matakuliah/{id}` | Menghapus mata kuliah | 200 |

Respons error:

| Kondisi | Status | Contoh body |
| --- | --- | --- |
| Field wajib tidak diisi | 400 | `{"error": "Field sks wajib diisi!"}` |
| SKS/semester <= 0 atau bukan bilangan bulat | 400 | `{"error": "Field sks harus lebih besar dari 0!"}` |
| `kode_mk` duplikat | 400 | `{"error": "Kode mata kuliah IF2110 sudah terdaftar!"}` |
| ID tidak ditemukan | 404 | `{"error": "Mata kuliah dengan ID 4 tidak ditemukan"}` |

### Contoh Pengujian dengan cURL

```bash
# READ ALL - Mahasiswa
curl -X GET http://localhost:6543/api/mahasiswa

# READ ONE - Mahasiswa
curl -X GET http://localhost:6543/api/mahasiswa/1

# CREATE - Mahasiswa
curl -X POST http://localhost:6543/api/mahasiswa \
  -H "Content-Type: application/json" \
  -d '{"nim":"67890","nama":"Ahmad Fadli","jurusan":"Teknik Elektro",
       "tanggal_lahir":"2001-11-05","alamat":"Jl. Mawar No. 10, Surabaya"}'

# UPDATE - Mahasiswa
curl -X PUT http://localhost:6543/api/mahasiswa/1 \
  -H "Content-Type: application/json" \
  -d '{"jurusan":"Informatika Medis"}'

# DELETE - Mahasiswa
curl -X DELETE http://localhost:6543/api/mahasiswa/3

# READ ALL - Matakuliah
curl -X GET http://localhost:6543/api/matakuliah

# CREATE - Matakuliah
curl -X POST http://localhost:6543/api/matakuliah \
  -H "Content-Type: application/json" \
  -d '{"kode_mk":"IF4020","nama_mk":"Kecerdasan Buatan",
       "sks":3,"semester":6}'

# UPDATE - Matakuliah
curl -X PUT http://localhost:6543/api/matakuliah/1 \
  -H "Content-Type: application/json" \
  -d '{"sks":4,"semester":4}'

# DELETE - Matakuliah
curl -X DELETE http://localhost:6543/api/matakuliah/4
```

Pada Windows Command Prompt, gunakan tanda kutip ganda yang di-escape
(`-d "{\"kode_mk\":\"IF4020\",...}"`) atau gunakan VS Code REST Client /
Postman agar payload JSON lebih mudah ditulis.

### Bukti Tangkapan Layar Pengujian

#### 1. Setup database, migrasi Alembic, dan seeding

![Setup database dan migrasi](screenshots/01_setup_database_migrasi.png)

#### 2. API Mahasiswa - Read All dan Read One (GET)

![API Mahasiswa GET](screenshots/02_mahasiswa_read.png)

#### 3. API Mahasiswa - Create, Validation, Update, Delete

![API Mahasiswa POST PUT DELETE](screenshots/03_mahasiswa_write.png)

#### 4. API Matakuliah - Read All dan Read One (GET)

![API Matakuliah GET](screenshots/04_matakuliah_read.png)

#### 5. API Matakuliah - Create, Validation, Update, Delete

![API Matakuliah POST PUT DELETE](screenshots/05_matakuliah_write.png)

#### 6. Pengujian otomatis pytest

![Hasil pytest](screenshots/06_pytest.png)

### Pengujian Otomatis

Selain pengujian manual dengan cURL, tersedia 15 pengujian otomatis
(WebTest + pytest) yang mencakup seluruh operasi CRUD, validasi input,
serta respons 400 dan 404:

```bash
pytest -q
```

Hasil:

```text
15 passed
```

### Catatan Implementasi

- **Model** `Mahasiswa` dan `Matakuliah` mewarisi `Base` dari `meta.py`,
  masing-masing memiliki method `to_dict()` untuk serialisasi JSON.
- **Registrasi model** dilakukan di `models/__init__.py` agar metadata
  tabel dikenali oleh Alembic dan SQLAlchemy.
- **Migrasi** dibuat dengan `alembic revision --autogenerate` sehingga
  sesuai dengan model Python, lalu diterapkan dengan `upgrade head`.
- **Routes** memakai predikat `request_method` agar path yang sama
  (`/api/mahasiswa` dan `/api/matakuliah`) dapat melayani GET dan POST
  secara tepat.
- **Validasi Matakuliah**: `kode_mk`, `nama_mk`, `sks`, dan `semester`
  wajib diisi; `sks` dan `semester` harus bilangan bulat lebih besar
  dari 0; `kode_mk` tidak boleh duplikat (dicek sebelum INSERT dan
  dilindungi juga oleh `UNIQUE constraint`).
- **Transaksi** ditangani otomatis oleh `pyramid_tm` dan
  `zope.sqlalchemy`; `dbsession.flush()` dipakai agar nilai `id` hasil
  autoincrement langsung tersedia pada respons.
- Kode ditulis mengikuti konvensi **PEP 8** (maksimal 79 karakter per
  baris, penamaan `snake_case`, impor terurut).

### Troubleshooting

| Masalah | Solusi |
| --- | --- |
| `psql` tidak dikenali | Tambahkan `C:\Program Files\PostgreSQL\16\bin` ke PATH |
| `password authentication failed` | Periksa password pada `sqlalchemy.url` dan user PostgreSQL |
| `permission denied for schema public` | Jalankan `GRANT ALL ON SCHEMA public TO pyramid_user;` |
| `Target database is not up to date` | Jalankan `alembic -c development.ini upgrade head` |
| Port 6543 sudah dipakai | Hentikan proses lain atau ubah `listen` pada `[server:main]` |
