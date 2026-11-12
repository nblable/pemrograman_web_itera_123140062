# ==============================================================================
# Berkas: member.py
# Deskripsi: Class Member untuk pengguna perpustakaan
# ==============================================================================

class Member:
    def __init__(self, member_id: str, nama: str, email: str):
        self.member_id = member_id
        self.nama = nama
        self._email = email
        # Private: daftar item yang sedang dipinjam (list id)
        self.__pinjam_list = []

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, nilai_baru: str):
        if "@" not in nilai_baru:
            raise ValueError("Format email tidak valid!")
        self._email = nilai_baru

    @property
    def jumlah_pinjam(self) -> int:
        return len(self.__pinjam_list)

    def pinjam_item(self, item) -> bool:
        if item.pinjam():
            self.__pinjam_list.append(item.item_id)
            return True
        return False

    def kembalikan_item(self, item) -> bool:
        if item.item_id in self.__pinjam_list:
            item.kembalikan()
            self.__pinjam_list.remove(item.item_id)
            return True
        return False

    def daftar_pinjam(self) -> list:
        return list(self.__pinjam_list)

    def __str__(self) -> str:
        return f"Member[{self.member_id}] {self.nama} ({self.email}) - Pinjam: {self.jumlah_pinjam} item"
