# Catatan Kuliah — Nabila Ramadhani Mujahidin (123140062)

Praktikum Pengembangan Aplikasi Web — Pertemuan 2: JavaScript Next Gen (ES6+)
Teknik Informatika · ITERA · T.A. 2026/2027

---

## 1. Tentang Aplikasi

Aplikasi **Catatan Kuliah** sederhana untuk menyimpan catatan materi kuliah harian.
Tampilan memakai CSS murni (tanpa framework) berwarna **pink**.

Fitur:

- Tulis catatan baru (judul + isi catatan panjang)
- Edit catatan (tombol Edit, formulir terisi otomatis)
- Hapus catatan (tombol Hapus)
- Catatan tersimpan otomatis di `localStorage`
- Kutipan motivasi acak dari API DummyJSON memakai Promise (`.then`/`.catch`), bisa dimuat ulang
- Jam berjalan di kop halaman

## 2. Cara Menjalankan

1. Buka folder ini di VS Code.
2. Klik kanan `index.html` → **Open with Live Server** (jangan double-click, karena `type="module"` diblokir CORS).
3. Buka `http://127.0.0.1:5500` di browser.

## 3. Struktur Folder

```text
nabilaramadhanimujahidin_123140062_pertemuan2/
├── index.html
├── README.md
├── css/style.css        seluruh tampilan (CSS murni)
├── docs/
│   ├── CARA_BUAT_SCREENSHOT.md
│   └── screenshot.png
└── js/
    ├── main.js          entry point (event + DOM)
    ├── app.js           class TaskItem & DashboardApp
    └── modules/
        ├── utils.js     fungsi bantuan
        └── data.js      catatan awal
```

## 4. Screenshot

Simpan screenshot hasil run di `docs/screenshot.png` (lihat `docs/CARA_BUAT_SCREENSHOT.md`).

![Tampilan aplikasi](docs/screenshot.png)

## 5. Fitur ES6+ dan Lokasi Kodenya

| Fitur ES6+ | Penjelasan | File : Baris |
|---|---|---|
| `const` | Konstanta (URL API, key storage, elemen DOM) | `js/main.js:5–7`, `js/modules/utils.js:5–15`, `js/app.js:63–64` |
| `let` | Variabel mode edit yang berubah | `js/main.js:9` (`idSedangEdit`) |
| Arrow function | Fungsi pendek | `js/modules/utils.js:5, 8, 15` · `js/main.js:12, 26, 42, 53` · `js/app.js:41, 45, 56` |
| Template literals | Merender HTML kartu catatan | `js/app.js:64, 72–83` · `js/main.js:14–20, 33–34` |
| Destructuring | Membongkar properti objek | `js/app.js:41, 73` · `js/main.js:33, 45` |
| Spread operator | Update array state immutable | `js/app.js:36, 41` · `js/main.js:104` |
| Classes | `TaskItem` (model) & `DashboardApp` (pengelola) | `js/app.js:6` dan `js/app.js:16` |
| Promise (`.then`/`.catch`) | Ambil kutipan dari API | `js/app.js:55–59` · `js/main.js:26–40` |
| localStorage | Simpan/muat data catatan | `js/app.js:25–30` |
| Modern array methods | `.map()`, `.filter()`, `.find()` | `js/app.js:41, 45, 49, 56, 62` |
| ES Modules | `import`/`export` | `js/app.js:3` · `js/main.js:3–4` |

## 6. API yang Digunakan

- DummyJSON Quotes: `https://dummyjson.com/quotes/random` — kutipan motivasi acak (Promise).

## 7. Pemenuhan Kriteria Penilaian

- Fungsionalitas dan interaktivitas (30%) — tambah, edit, hapus catatan.
- Fitur ES6+ (25%) — lihat tabel bagian 5.
- localStorage dan pengelolaan data (20%) — `js/app.js:25–30`.
- Desain UI dan UX (15%) — layout grid CSS murni berwarna pink, kartu catatan, responsif.
- Dokumentasi dan kerapian kode (10%) — README dan komentar di setiap file.
