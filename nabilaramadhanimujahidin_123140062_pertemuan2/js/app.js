// js/app.js
// Class TaskItem (model catatan) dan DashboardApp (pengelola data + API)
import { buatId, formatWaktu, amanTeks } from "./modules/utils.js";

// Model satu catatan
export class TaskItem {
  constructor({ id = buatId(), judul = "", isi = "", waktu = formatWaktu() }) {
    this.id = id;
    this.judul = judul;
    this.isi = isi;
    this.waktu = waktu;
  }
}

// Pengelola aplikasi: data, localStorage, dan ambil kutipan
export class DashboardApp {
  constructor(kunciSimpan, urlKutipan) {
    this.kunciSimpan = kunciSimpan;
    this.urlKutipan = urlKutipan;
    this.catatan = [];
  }

  // ---- localStorage ----
  muatCatatan() {
    const data = localStorage.getItem(this.kunciSimpan);
    this.catatan = data ? JSON.parse(data) : [];
  }

  simpanCatatan() {
    localStorage.setItem(this.kunciSimpan, JSON.stringify(this.catatan));
  }

  // ---- operasi data ----
  tambahCatatan({ judul, isi }) {
    const catatanBaru = new TaskItem({ judul, isi });
    this.catatan = [...this.catatan, catatanBaru]; // spread operator
    this.simpanCatatan();
  }

  ubahCatatan(id, { judul, isi }) {
    this.catatan = this.catatan.map((c) => (c.id === id ? { ...c, judul, isi } : c)); // spread + destructuring
    this.simpanCatatan();
  }

  hapusCatatan(id) {
    this.catatan = this.catatan.filter((c) => c.id !== id);
    this.simpanCatatan();
  }

  cariCatatan(id) {
    return this.catatan.find((c) => c.id === id);
  }

  // ---- operasi asinkron: ambil kutipan memakai Promise (.then / .catch) ----
  ambilKutipan() {
    return fetch(this.urlKutipan)
      .then((respon) => respon.json())
      .then((data) => ({ teks: data.quote, penulis: data.author }));
  }

  // ---- tampilkan ke layar (template literals) ----
  tampilkanCatatan() {
    const wadah = document.getElementById("daftarCatatan");
    const jumlah = document.getElementById("jumlahCatatan");
    jumlah.textContent = `${this.catatan.length} catatan`;

    if (this.catatan.length === 0) {
      wadah.innerHTML = `<p class="catatan-kosong">Belum ada catatan.</p>`;
      return;
    }

    wadah.innerHTML = this.catatan
      .map((c) => {
        const { id, judul, isi, waktu } = c;
        return `
          <article class="catatan">
            <h3>${amanTeks(judul)}</h3>
            <p class="isi-teks">${amanTeks(isi)}</p>
            <p class="waktu">${amanTeks(waktu)}</p>
            <div class="aksi">
              <button type="button" class="tombol-kecil" data-aksi="edit" data-id="${id}">Edit</button>
              <button type="button" class="tombol-kecil" data-aksi="hapus" data-id="${id}">Hapus</button>
            </div>
          </article>`;
      })
      .join("");
  }
}
