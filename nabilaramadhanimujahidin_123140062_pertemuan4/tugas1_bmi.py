# ===================================================
# Berkas: tugas1_bmi.py
# Deskripsi: Program penghitung Body Mass Index (BMI) sederhana
# ===================================================

"""Program penghitung Body Mass Index (BMI).

Menghitung nilai BMI berdasarkan berat badan (kg) dan tinggi badan (m),
kemudian menentukan kategori status berat badan.
"""


def hitung_bmi(berat_kg: float, tinggi_m: float) -> float:
    """Menghitung nilai BMI menggunakan rumus berat / (tinggi * tinggi).

    Args:
        berat_kg (float): Berat badan dalam kilogram.
        tinggi_m (float): Tinggi badan dalam meter.

    Returns:
        float: Nilai BMI yang dihitung.
    """
    if tinggi_m <= 0:
        raise ValueError("Tinggi badan harus lebih dari 0.")
    return berat_kg / (tinggi_m * tinggi_m)


def kategori_bmi(bmi: float) -> str:
    """Menentukan kategori status berat badan berdasarkan nilai BMI.

    Args:
        bmi (float): Nilai BMI yang telah dihitung.

    Returns:
        str: Kategori status berat badan.
    """
    if bmi < 18.5:
        return "Berat badan kurang"
    elif bmi < 25:
        return "Berat badan normal"
    elif bmi < 30:
        return "Berat badan berlebih"
    else:
        return "Obesitas"


def main() -> None:
    """Fungsi utama program penghitung BMI."""
    print("--- PROGRAM PENGHITUNG BMI ---")
    try:
        berat_kg = float(input("Masukkan berat badan (kg) : "))
        tinggi_m = float(input("Masukkan tinggi badan (m)  : "))
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        return

    if berat_kg <= 0 or tinggi_m <= 0:
        print("Berat dan tinggi badan harus lebih dari 0.")
        return

    bmi = hitung_bmi(berat_kg, tinggi_m)
    kategori = kategori_bmi(bmi)

    print("\n--- HASIL PERHITUNGAN ---")
    print(f"Berat badan : {berat_kg:.2f} kg")
    print(f"Tinggi badan: {tinggi_m:.2f} m")
    print(f"Nilai BMI   : {bmi:.2f}")
    print(f"Kategori    : {kategori}")


if __name__ == "__main__":
    main()