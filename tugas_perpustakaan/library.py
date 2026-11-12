# ==============================================================================
# Berkas: library.py
# Deskripsi: Class Library untuk mengelola koleksi item perpustakaan
# ==============================================================================

class Library:
    def __init__(self, nama: str):
        self.nama = nama
        # Private: koleksi item perpustakaan
        self.__koleksi = []

    @property
    def total_item(self) -> int:
        return len(self.__koleksi)

    def tambah_item(self, item) -> bool:
        for existing in self.__koleksi:
            if existing.item_id == item.item_id:
                print(f"Item dengan ID '{item.item_id}' sudah ada di koleksi.")
                return False
        self.__koleksi.append(item)
        print(f"Item '{item.judul}' berhasil ditambahkan ke perpustakaan.")
        return True

    def tampilkan_katalog(self):
        if not self.__koleksi:
            print("Katalog perpustakaan masih kosong.")
            return
        print(f"\n===== KATALOG {self.nama.upper()} =====")
        for item in self.__koleksi:
            print(item)
            print("   " + item.get_detail())

    def tampilkan_tersedia(self):
        print("\n--- Item yang Tersedia ---")
        ada = False
        for item in self.__koleksi:
            if not item.is_dipinjam:
                print(item)
                ada = True
        if not ada:
            print("Tidak ada item yang tersedia saat ini.")

    def cari_by_id(self, item_id: str):
        for item in self.__koleksi:
            if item.item_id == item_id:
                return item
        return None

    def cari_by_judul(self, keyword: str) -> list:
        hasil = []
        for item in self.__koleksi:
            if keyword.lower() in item.judul.lower():
                hasil.append(item)
        return hasil

    def hitung_total_denda(self, hari_terlambat: int) -> float:
        # Polimorfik: setiap item menghitung denda sesuai jenisnya
        total = 0.0
        for item in self.__koleksi:
            total += item.hitung_denda(hari_terlambat)
        return total
