# ==============================================================================
# Berkas: main.py
# Deskripsi: Skrip eksekusi untuk menguji sistem perpustakaan
# ==============================================================================

from library_item import Book, Magazine
from member import Member
from library import Library

if __name__ == "__main__":
    # 1. Buat perpustakaan
    perpus = Library("Perpustakaan ITERA")

    # 2. Tambahkan beberapa buku dan majalah
    b1 = Book("B001", "Pemrograman Web dengan Python", 2024,
              "Ahmad Fadhil", "978-1234567890", 320)
    b2 = Book("B002", "Struktur Data dan Algoritma", 2023,
              "Siti Rahma", "978-0987654321", 450)
    m1 = Magazine("M001", "InfoTeknologi", 2025, "Edisi 12", "ITERA Press")
    m2 = Magazine("M002", "Sains Populer", 2024, "Edisi 5", "Sains Indonesia")

    perpus.tambah_item(b1)
    perpus.tambah_item(b2)
    perpus.tambah_item(m1)
    perpus.tambah_item(m2)

    # Coba tambah item dengan ID duplikat
    perpus.tambah_item(Book("B001", "Duplikat", 2024, "X", "0", 10))

    # 3. Tampilkan katalog
    perpus.tampilkan_katalog()
    print(f"\nTotal item di perpustakaan: {perpus.total_item}")

    # 4. Cari item berdasarkan id dan judul
    print("\n--- Pencarian Item ---")
    cari_id = perpus.cari_by_id("B002")
    if cari_id:
        print("Ditemukan (by ID):", cari_id.get_detail())
    else:
        print("Item dengan ID tersebut tidak ditemukan.")

    hasil_judul = perpus.cari_by_judul("python")
    print("Hasil pencarian judul 'python':")
    for item in hasil_judul:
        print(" -", item)

    # 5. Demonstrasi peminjaman oleh member
    print("\n--- Peminjaman ---")
    member = Member("M001", "Nabila Ramadhani Mujahidin", "nabila@itera.ac.id")
    if member.pinjam_item(b1):
        print(f"{member.nama} berhasil meminjam: {b1.judul}")
    else:
        print(f"Gagal meminjam: {b1.judul}")

    # Coba pinjam item yang sama lagi
    if member.pinjam_item(b1):
        print("Berhasil pinjam lagi (seharusnya gagal).")
    else:
        print(f"Item '{b1.judul}' sedang dipinjam, tidak bisa dipinjam lagi.")

    print(member)
    print("Daftar pinjam member:", member.daftar_pinjam())

    # 6. Tampilkan item yang tersedia
    perpus.tampilkan_tersedia()

    # 7. Pengembalian item
    print("\n--- Pengembalian ---")
    if member.kembalikan_item(b1):
        print(f"{member.nama} berhasil mengembalikan: {b1.judul}")
    print(member)

    # 8. Demonstrasi polymorphism: hitung denda
    print("\n--- Perhitungan Denda (Polymorphism) ---")
    hari = 5
    for item in [b1, b2, m1]:
        print(f"{item.judul}: denda {hari} hari = Rp {item.hitung_denda(hari):,.0f}")
    print(f"Total denda semua item (5 hari): Rp {perpus.hitung_total_denda(hari):,.0f}")

    # 9. Demonstrasi property setter email
    print("\n--- Uji Property Setter ---")
    try:
        member.email = "email_tanpa_at"
    except ValueError as err:
        print(f"Validasi email: {err}")
    member.email = "nabila.baru@itera.ac.id"
    print("Email member sekarang:", member.email)
