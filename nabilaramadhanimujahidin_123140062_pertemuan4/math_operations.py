# ===================================================
# Berkas: math_operations.py
# Deskripsi: Modul matematika berisi fungsi geometri dan konversi suhu
# ===================================================

"""Modul matematika kustom.

Menyediakan fungsi perhitungan luas dan keliling bentuk geometri
serta fungsi konversi temperatur suhu.
"""

PI = 3.14159


def luas_persegi(sisi: float) -> float:
    """Menghitung luas persegi.

    Args:
        sisi (float): Panjang sisi persegi.

    Returns:
        float: Luas persegi.
    """
    return sisi * sisi


def keliling_persegi(sisi: float) -> float:
    """Menghitung keliling persegi.

    Args:
        sisi (float): Panjang sisi persegi.

    Returns:
        float: Keliling persegi.
    """
    return 4 * sisi


def luas_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung luas persegi panjang.

    Args:
        panjang (float): Panjang persegi panjang.
        lebar (float): Lebar persegi panjang.

    Returns:
        float: Luas persegi panjang.
    """
    return panjang * lebar


def keliling_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung keliling persegi panjang.

    Args:
        panjang (float): Panjang persegi panjang.
        lebar (float): Lebar persegi panjang.

    Returns:
        float: Keliling persegi panjang.
    """
    return 2 * (panjang + lebar)


def luas_lingkaran(jari_jari: float) -> float:
    """Menghitung luas lingkaran.

    Args:
        jari_jari (float): Jari-jari lingkaran.

    Returns:
        float: Luas lingkaran.
    """
    return PI * jari_jari * jari_jari


def keliling_lingkaran(jari_jari: float) -> float:
    """Menghitung keliling (circumference) lingkaran.

    Args:
        jari_jari (float): Jari-jari lingkaran.

    Returns:
        float: Keliling lingkaran.
    """
    return 2 * PI * jari_jari


def celsius_ke_fahrenheit(celsius: float) -> float:
    """Mengkonversi suhu dari Celsius ke Fahrenheit.

    Formula: F = C * 9/5 + 32.

    Args:
        celsius (float): Suhu dalam derajat Celsius.

    Returns:
        float: Suhu dalam derajat Fahrenheit.
    """
    return celsius * 9 / 5 + 32


def celsius_ke_kelvin(celsius: float) -> float:
    """Mengkonversi suhu dari Celsius ke Kelvin.

    Formula: K = C + 273.15.

    Args:
        celsius (float): Suhu dalam derajat Celsius.

    Returns:
        float: Suhu dalam Kelvin.
    """
    return celsius + 273.15


if __name__ == "__main__":
    print("[TEST MODUL] Uji coba internal math_operations:")
    print("Luas persegi (sisi=4)      :", luas_persegi(4))
    print("Keliling lingkaran (r=7)   :", keliling_lingkaran(7))
    print("100 C -> F                 :", celsius_ke_fahrenheit(100))
    print("100 C -> K                 :", celsius_ke_kelvin(100))