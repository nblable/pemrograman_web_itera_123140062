// js/modules/utils.js
// Fungsi bantuan sederhana (arrow function)

// Bikin ID unik sederhana
export const buatId = () => "_" + Math.random().toString(36).slice(2, 9);

// Format waktu sekarang jadi 16 Okt 2026, 14.30
export const formatWaktu = () => {
  const sekarang = new Date();
  const jam = sekarang.toLocaleTimeString("id-ID", { hour: "2-digit", minute: "2-digit" });
  return `${sekarang.toLocaleDateString("id-ID")}, ${jam}`;
};

// Ganti karakter berbahaya supaya aman jadi HTML
export const amanTeks = (teks) => String(teks).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
