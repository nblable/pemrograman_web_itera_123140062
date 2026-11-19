# ===================================================
# Berkas: tugas2_nilai_mahasiswa.py
# Deskripsi: Program pengelolaan data nilai mahasiswa
# ===================================================

"""Program pengelolaan data nilai mahasiswa.

Menghitung nilai akhir berdasarkan bobot UTS, UAS, dan Tugas,
menentukan grade, serta menampilkan mahasiswa dengan nilai
tertinggi dan terendah.
"""


def hitung_nilai_akhir(uts: float, uas: float, tugas: float) -> float:
    """Menghitung nilai akhir mahasiswa.

    Nilai Akhir = (30% * UTS) + (40% * UAS) + (30% * Tugas).

    Args:
        uts (float): Nilai UTS.
        uas (float): Nilai UAS.
        tugas (float): Nilai Tugas.

    Returns:
        float: Nilai akhir mahasiswa.
    """
    return (0.30 * uts) + (0.40 * uas) + (0.30 * tugas)


def tentukan_grade(nilai_akhir: float) -> str:
    """Menentukan grade berdasarkan nilai akhir.

    Args:
        nilai_akhir (float): Nilai akhir mahasiswa.

    Returns:
        str: Grade (A-E).
    """
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"


def main() -> None:
    """Fungsi utama program pengelolaan nilai mahasiswa."""
    data_mahasiswa = [
        {"nama": "Nabila", "nim": "123140062",
         "nilai_uts": 85, "nilai_uas": 90, "nilai_tugas": 88},
        {"nama": "Budi Santoso", "nim": "123140001",
         "nilai_uts": 70, "nilai_uas": 75, "nilai_tugas": 68},
        {"nama": "Siti Aminah", "nim": "123140002",
         "nilai_uts": 92, "nilai_uas": 88, "nilai_tugas": 95},
        {"nama": "Andi Wijaya", "nim": "123140003",
         "nilai_uts": 55, "nilai_uas": 60, "nilai_tugas": 58},
        {"nama": "Dewi Lestari", "nim": "123140004",
         "nilai_uts": 40, "nilai_uas": 45, "nilai_tugas": 50},
    ]

    # Hitung nilai akhir dan grade untuk setiap mahasiswa
    for mhs in data_mahasiswa:
        mhs["nilai_akhir"] = hitung_nilai_akhir(
            mhs["nilai_uts"], mhs["nilai_uas"], mhs["nilai_tugas"]
        )
        mhs["grade"] = tentukan_grade(mhs["nilai_akhir"])

    # Tampilkan tabel
    print("--- DATA NILAI MAHASISWA ---")
    header = f"{'No':<4}{'Nama':<16}{'NIM':<12}{'UTS':<6}{'UAS':<6}{'Tugas':<7}{'Akhir':<8}{'Grade':<6}"
    print(header)
    print("-" * len(header))
    for idx, mhs in enumerate(data_mahasiswa, start=1):
        print(
            f"{idx:<4}{mhs['nama']:<16}{mhs['nim']:<12}"
            f"{mhs['nilai_uts']:<6}{mhs['nilai_uas']:<6}{mhs['nilai_tugas']:<7}"
            f"{mhs['nilai_akhir']:<8.2f}{mhs['grade']:<6}"
        )

    # Cari nilai tertinggi dan terendah
    tertinggi = max(data_mahasiswa, key=lambda m: m["nilai_akhir"])
    terendah = min(data_mahasiswa, key=lambda m: m["nilai_akhir"])

    print("\n--- NILAI TERTINGGI ---")
    print(f"Nama       : {tertinggi['nama']}")
    print(f"NIM        : {tertinggi['nim']}")
    print(f"Nilai Akhir: {tertinggi['nilai_akhir']:.2f}")
    print(f"Grade      : {tertinggi['grade']}")

    print("\n--- NILAI TERENDAH ---")
    print(f"Nama       : {terendah['nama']}")
    print(f"NIM        : {terendah['nim']}")
    print(f"Nilai Akhir: {terendah['nilai_akhir']:.2f}")
    print(f"Grade      : {terendah['grade']}")


if __name__ == "__main__":
    main()