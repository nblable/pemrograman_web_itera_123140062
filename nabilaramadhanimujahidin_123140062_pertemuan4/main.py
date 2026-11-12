"""Program utama yang menggunakan modul math_operations.

Menerapkan dua cara berbeda untuk mengimpor modul/fungsi:
1. import math_operations (akses dengan prefix)
2. from math_operations import ... (akses langsung)
"""

# Cara 1: mengimpor seluruh modul
import math_operations as mo

# Cara 2: mengimpor fungsi spesifik langsung
from math_operations import celsius_ke_fahrenheit, celsius_ke_kelvin


def main() -> None:
    """Fungsi utama program."""
    print("=== PROGRAM KALKULATOR MATEMATIKA ===")

    # --- Geometri (menggunakan modul dengan prefix) ---
    print("\n--- BENTUK GEOMETRI ---")
    sisi = 5.0
    print(f"Persegi (sisi={sisi}):")
    print(f"  Luas     = {mo.luas_persegi(sisi):.2f}")
    print(f"  Keliling = {mo.keliling_persegi(sisi):.2f}")

    panjang, lebar = 8.0, 4.0
    print(f"\nPersegi Panjang (p={panjang}, l={lebar}):")
    print(f"  Luas     = {mo.luas_persegi_panjang(panjang, lebar):.2f}")
    print(f"  Keliling = {mo.keliling_persegi_panjang(panjang, lebar):.2f}")

    r = 7.0
    print(f"\nLingkaran (r={r}):")
    print(f"  Luas     = {mo.luas_lingkaran(r):.2f}")
    print(f"  Keliling = {mo.keliling_lingkaran(r):.2f}")
    print(f"  Konstanta PI = {mo.PI}")

    # --- Konversi suhu (menggunakan fungsi yang diimpor langsung) ---
    print("\n--- KONVERSI SUHU ---")
    celsius = 30.0
    print(f"{celsius:.2f} C = {celsius_ke_fahrenheit(celsius):.2f} F")
    print(f"{celsius:.2f} C = {celsius_ke_kelvin(celsius):.2f} K")

    celsius2 = 0.0
    print(f"{celsius2:.2f} C = {celsius_ke_fahrenheit(celsius2):.2f} F")
    print(f"{celsius2:.2f} C = {celsius_ke_kelvin(celsius2):.2f} K")

    print("\n=== SELESAI ===")


if __name__ == "__main__":
    main()