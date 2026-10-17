// js/main.js
// Entry point: DOM, event, dan pemanggilan fungsi
import { DashboardApp } from "./app.js";
import { catatanAwal } from "./modules/data.js";

const app = new DashboardApp("catatan_nabila_123140062", "https://dummyjson.com/quotes/random");

// Variabel mode edit (berubah-ubah nilainya, jadi pakai let)
let idSedangEdit = "";

// ---- jam sederhana ----
const jalankanJam = () => {
  document.getElementById("jam").textContent = new Date().toLocaleString("id-ID", {
    weekday: "long",
    day: "numeric",
    month: "long",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  });
};
setInterval(jalankanJam, 1000);

// ---- ambil kutipan memakai Promise (.then / .catch) ----
const muatKutipan = () => {
  const teks = document.getElementById("teksKutipan");
  const penulis = document.getElementById("penulisKutipan");
  app
    .ambilKutipan()
    .then(({ teks: isiKutipan, penulis: namaPenulis }) => {
      // destructuring hasil Promise
      teks.textContent = `"${isiKutipan}"`;
      penulis.textContent = `— ${namaPenulis}`;
    })
    .catch(() => {
      teks.textContent = "Kutipan gagal dimuat.";
    });
};

// ---- isi form saat klik edit ----
const mulaiEdit = (id) => {
  const catatan = app.cariCatatan(id);
  idSedangEdit = id;
  document.getElementById("idCatatan").value = id;
  document.getElementById("judulCatatan").value = catatan.judul;
  document.getElementById("isiCatatan").value = catatan.isi;
  document.getElementById("judulForm").textContent = "Edit Catatan";
  document.getElementById("batalEdit").classList.add("tampil");
};

// ---- kembalikan form ke mode tambah ----
const batalEdit = () => {
  document.getElementById("formCatatan").reset();
  document.getElementById("idCatatan").value = "";
  idSedangEdit = "";
  document.getElementById("judulForm").textContent = "Tulis Catatan Baru";
  document.getElementById("batalEdit").classList.remove("tampil");
};

// ---- event: simpan catatan (tambah atau edit) ----
document.getElementById("formCatatan").addEventListener("submit", (event) => {
  event.preventDefault();

  const judul = document.getElementById("judulCatatan").value.trim();
  const isi = document.getElementById("isiCatatan").value.trim();

  if (!judul) return;

  if (idSedangEdit) {
    app.ubahCatatan(idSedangEdit, { judul, isi });
  } else {
    app.tambahCatatan({ judul, isi });
  }

  batalEdit();
  app.tampilkanCatatan();
});

document.getElementById("batalEdit").addEventListener("click", batalEdit);

// ---- event: edit / hapus catatan (delegasi) ----
document.getElementById("daftarCatatan").addEventListener("click", (event) => {
  const tombol = event.target.closest("[data-aksi]");
  if (!tombol) return;

  const { aksi, id } = tombol.dataset;

  if (aksi === "edit") mulaiEdit(id);
  if (aksi === "hapus") {
    app.hapusCatatan(id);
    app.tampilkanCatatan();
  }
});

// ---- event: tombol muat ulang kutipan ----
document.getElementById("tombolKutipan").addEventListener("click", muatKutipan);

// ---- mulai aplikasi ----
app.muatCatatan();

// kalau storage masih kosong, isi catatan awal
if (app.catatan.length === 0) {
  catatanAwal.forEach((c) => app.tambahCatatan({ ...c }));
}

app.tampilkanCatatan();
muatKutipan();
jalankanJam();
