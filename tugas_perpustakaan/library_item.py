# ==============================================================================
# Berkas: library_item.py
# Deskripsi: Abstract class LibraryItem beserta subclass Book dan Magazine
# ==============================================================================

from abc import ABC, abstractmethod


class LibraryItem(ABC):
    """Cetak biru (abstract) untuk semua item yang ada di perpustakaan."""

    def __init__(self, item_id: str, judul: str, tahun_terbit: int):
        # Protected attributes: boleh diakses subclass
        self._item_id = item_id
        self._judul = judul
        self._tahun_terbit = tahun_terbit
        # Private attribute: status peminjaman, terlindungi name mangling
        self.__dipinjam = False

    # ------------------------------------------------------------------
    # PROPERTY (getter) untuk atribut penting
    # ------------------------------------------------------------------
    @property
    def item_id(self) -> str:
        return self._item_id

    @property
    def judul(self) -> str:
        return self._judul

    @property
    def tahun_terbit(self) -> int:
        return self._tahun_terbit

    @property
    def is_dipinjam(self) -> bool:
        """Status ketersediaan item (read-only dari luar)."""
        return self.__dipinjam

    # ------------------------------------------------------------------
    # ABSTRACT METHODS: wajib diimplementasikan subclass
    # ------------------------------------------------------------------
    @abstractmethod
    def get_detail(self) -> str:
        """Mengembalikan detail lengkap item."""
        pass

    @abstractmethod
    def hitung_denda(self, hari_terlambat: int) -> float:
        """Menghitung denda keterlambatan pengembalian."""
        pass

    # ------------------------------------------------------------------
    # CONCRETE METHODS: logika umum yang dibagikan
    # ------------------------------------------------------------------
    def pinjam(self) -> bool:
        if self.__dipinjam:
            return False
        self.__dipinjam = True
        return True

    def kembalikan(self):
        self.__dipinjam = False

    def __str__(self) -> str:
        status = "Dipinjam" if self.__dipinjam else "Tersedia"
        return f"[{self._item_id}] {self._judul} ({self._tahun_terbit}) - {status}"

    def __eq__(self, other):
        if isinstance(other, LibraryItem):
            return self._item_id == other._item_id
        return False


class Book(LibraryItem):
    """Subclass untuk item berupa buku."""

    def __init__(self, item_id: str, judul: str, tahun_terbit: int,
                 pengarang: str, isbn: str, jumlah_halaman: int):
        super().__init__(item_id, judul, tahun_terbit)
        self.pengarang = pengarang
        self.isbn = isbn
        self.jumlah_halaman = jumlah_halaman
        self._kategori = "Buku"

    def get_detail(self) -> str:
        return (f"Buku: {self._judul} | Pengarang: {self.pengarang} | "
                f"ISBN: {self.isbn} | Halaman: {self.jumlah_halaman} | "
                f"Tahun: {self._tahun_terbit}")

    def hitung_denda(self, hari_terlambat: int) -> float:
        # Denda buku: Rp 2.000 per hari keterlambatan
        if hari_terlambat < 0:
            hari_terlambat = 0
        return hari_terlambat * 2000


class Magazine(LibraryItem):
    """Subclass untuk item berupa majalah."""

    def __init__(self, item_id: str, judul: str, tahun_terbit: int,
                 edisi: str, penerbit: str):
        super().__init__(item_id, judul, tahun_terbit)
        self.edisi = edisi
        self.penerbit = penerbit
        self._kategori = "Majalah"

    def get_detail(self) -> str:
        return (f"Majalah: {self._judul} | Edisi: {self.edisi} | "
                f"Penerbit: {self.penerbit} | Tahun: {self._tahun_terbit}")

    def hitung_denda(self, hari_terlambat: int) -> float:
        # Denda majalah: Rp 1.000 per hari keterlambatan
        if hari_terlambat < 0:
            hari_terlambat = 0
        return hari_terlambat * 1000
