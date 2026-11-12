"""Program penghitung Body Mass Index (BMI) sederhana.

Menghitung nilai BMI dari berat dan tinggi badan, lalu menentukan
kategori status berat badan berdasarkan standar BMI.
"""


def hitung_bmi(berat_kg: float, tinggi_m: float) -> float:
    """Menghitung nilai BMI.

    Args:
        berat_kg: Berat badan dalam kilogram.
        tinggi_m: Tinggi badan dalam meter.

    Returns:
        Nilai BMI (float).
    """
    if tinggi_m <= 0:
        raise ValueError("Tinggi badan harus lebih dari 0.")
    return berat_kg / (tinggi_m * tinggi_m)


def kategori_bmi(bmi: float) -> str:
    """Menentukan kategori BMI.

    Args:
        bmi: Nilai BMI yang sudah dihitung.

    Returns:
        String kategori status berat badan.
    """
    if bmi < 18.5:
        return "Berat badan kurang"
    if bmi < 25:
        return "Berat badan normal"
    if bmi < 30:
        return "Berat badan berlebih"
    return "Obesitas"


def main() -> None:
    """Fungsi utama program."""
    print("=== PENGHITUNG BMI (BODY MASS INDEX) ===")
    try:
        berat = float(input("Masukkan berat badan (kg): "))
        tinggi = float(input("Masukkan tinggi badan (m): "))
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        return

    if berat <= 0 or tinggi <= 0:
        print("Berat dan tinggi badan harus lebih dari 0.")
        return

    bmi = hitung_bmi(berat, tinggi)
    kategori = kategori_bmi(bmi)

    print(f"\nBerat badan : {berat:.2f} kg")
    print(f"Tinggi badan: {tinggi:.2f} m")
    print(f"Nilai BMI   : {bmi:.2f}")
    print(f"Kategori    : {kategori}")


if __name__ == "__main__":
    main()