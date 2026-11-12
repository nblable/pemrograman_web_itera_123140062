"""Program pengelolaan data nilai mahasiswa.

Menghitung nilai akhir berdasarkan bobot UTS, UAS, dan Tugas,
menentukan grade, menampilkan tabel, serta mencari nilai tertinggi
dan terendah.
"""


def hitung_nilai_akhir(nilai_uts: float, nilai_uas: float, nilai_tugas: float) -> float:
    """Menghitung nilai akhir dengan bobot 30% UTS, 40% UAS, 30% Tugas.

    Args:
        nilai_uts: Nilai Ujian Tengah Semester.
        nilai_uas: Nilai Ujian Akhir Semester.
        nilai_tugas: Nilai tugas.

    Returns:
        Nilai akhir (float).
    """
    return (0.30 * nilai_uts) + (0.40 * nilai_uas) + (0.30 * nilai_tugas)


def tentukan_grade(nilai_akhir: float) -> str:
    """Menentukan grade berdasarkan nilai akhir.

    Args:
        nilai_akhir: Nilai akhir mahasiswa.

    Returns:
        Grade (A, B, C, D, atau E).
    """
    if nilai_akhir >= 80:
        return "A"
    if nilai_akhir >= 70:
        return "B"
    if nilai_akhir >= 60:
        return "C"
    if nilai_akhir >= 50:
        return "D"
    return "E"


def main() -> None:
    """Fungsi utama program."""
    data_mahasiswa = [
        {"nama": "Andi Pratama", "nim": "123140001", "nilai_uts": 80, "nilai_uas": 85, "nilai_tugas": 90},
        {"nama": "Budi Santoso", "nim": "123140002", "nilai_uts": 65, "nilai_uas": 70, "nilai_tugas": 75},
        {"nama": "Citra Lestari", "nim": "123140003", "nilai_uts": 90, "nilai_uas": 95, "nilai_tugas": 88},
        {"nama": "Dewi Anggraini", "nim": "123140004", "nilai_uts": 55, "nilai_uas": 60, "nilai_tugas": 58},
        {"nama": "Eko Wijaya", "nim": "123140005", "nilai_uts": 72, "nilai_uas": 78, "nilai_tugas": 80},
    ]

    # Hitung nilai akhir dan grade untuk setiap mahasiswa
    for mhs in data_mahasiswa:
        mhs["nilai_akhir"] = hitung_nilai_akhir(
            mhs["nilai_uts"], mhs["nilai_uas"], mhs["nilai_tugas"]
        )
        mhs["grade"] = tentukan_grade(mhs["nilai_akhir"])

    # Tampilkan tabel
    print("=== DATA NILAI MAHASISWA ===")
    print(f"{'No':<4}{'Nama':<18}{'NIM':<12}{'UTS':<6}{'UAS':<6}{'Tugas':<8}{'Akhir':<8}{'Grade':<6}")
    print("-" * 68)
    for i, mhs in enumerate(data_mahasiswa, start=1):
        print(
            f"{i:<4}{mhs['nama']:<18}{mhs['nim']:<12}"
            f"{mhs['nilai_uts']:<6}{mhs['nilai_uas']:<6}{mhs['nilai_tugas']:<8}"
            f"{mhs['nilai_akhir']:<8.2f}{mhs['grade']:<6}"
        )

    # Cari nilai tertinggi dan terendah
    tertinggi = max(data_mahasiswa, key=lambda m: m["nilai_akhir"])
    terendah = min(data_mahasiswa, key=lambda m: m["nilai_akhir"])

    print("\n=== HASIL ANALISIS ===")
    print(
        f"Nilai tertinggi: {tertinggi['nama']} (NIM: {tertinggi['nim']}) "
        f"-> {tertinggi['nilai_akhir']:.2f} (Grade {tertinggi['grade']})"
    )
    print(
        f"Nilai terendah : {terendah['nama']} (NIM: {terendah['nim']}) "
        f"-> {terendah['nilai_akhir']:.2f} (Grade {terendah['grade']})"
    )


if __name__ == "__main__":
    main()