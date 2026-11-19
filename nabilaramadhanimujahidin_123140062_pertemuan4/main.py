# ===================================================
# Berkas: main.py
# Deskripsi: Program utama pengguna modul math_operations
# ===================================================

"""Program utama yang menggunakan modul math_operations.

Menerapkan dua cara berbeda untuk mengimpor modul/fungsi:
1. import math_operations
2. from math_operations import ...
"""

# Cara 1: Mengimpor seluruh modul
import math_operations

# Cara 2: Mengimpor fungsi spesifik langsung ke namespace
from math_operations import luas_lingkaran, keliling_lingkaran, PI


def main() -> None:
    """Fungsi utama program."""
    print("--- PROGRAM MATEMATIKA ---")

    # Menggunakan modul yang diimpor secara penuh (cara 1)
    print("\n[1] Geometri - Persegi")
    sisi = 5.0
    print(f"Sisi persegi     : {sisi}")
    print(f"Luas persegi     : {math_operations.luas_persegi(sisi)}")
    print(f"Keliling persegi : {math_operations.keliling_persegi(sisi)}")

    print("\n[2] Geometri - Persegi Panjang")
    panjang, lebar = 8.0, 4.0
    print(f"Panjang x Lebar  : {panjang} x {lebar}")
    print(f"Luas             : {math_operations.luas_persegi_panjang(panjang, lebar)}")
    print(f"Keliling         : {math_operations.keliling_persegi_panjang(panjang, lebar)}")

    # Menggunakan fungsi yang diimpor langsung (cara 2)
    print("\n[3] Geometri - Lingkaran")
    r = 7.0
    print(f"Jari-jari        : {r}")
    print(f"Konstanta PI     : {PI}")
    print(f"Luas lingkaran   : {luas_lingkaran(r)}")
    print(f"Keliling lingkaran: {keliling_lingkaran(r)}")

    # Konversi suhu (cara 1)
    print("\n[4] Konversi Suhu")
    celsius = 25.0
    print(f"Suhu awal (C)    : {celsius}")
    print(f"Ke Fahrenheit    : {math_operations.celsius_ke_fahrenheit(celsius):.2f} F")
    print(f"Ke Kelvin        : {math_operations.celsius_ke_kelvin(celsius):.2f} K")

    # Uji tambahan
    print("\n[5] Uji Tambahan Konversi Suhu")
    for c in (0, 37, 100):
        f = math_operations.celsius_ke_fahrenheit(c)
        k = math_operations.celsius_ke_kelvin(c)
        print(f"{c:>3} C  ->  {f:>7.2f} F  |  {k:>7.2f} K")


if __name__ == "__main__":
    main()