"""Modul matematika: fungsi geometri, konversi suhu, dan konstanta."""

PI = 3.14159


def luas_persegi(sisi: float) -> float:
    """Menghitung luas persegi.

    Args:
        sisi: Panjang sisi persegi.

    Returns:
        Luas persegi.
    """
    return sisi * sisi


def keliling_persegi(sisi: float) -> float:
    """Menghitung keliling persegi.

    Args:
        sisi: Panjang sisi persegi.

    Returns:
        Keliling persegi.
    """
    return 4 * sisi


def luas_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung luas persegi panjang.

    Args:
        panjang: Panjang persegi panjang.
        lebar: Lebar persegi panjang.

    Returns:
        Luas persegi panjang.
    """
    return panjang * lebar


def keliling_persegi_panjang(panjang: float, lebar: float) -> float:
    """Menghitung keliling persegi panjang.

    Args:
        panjang: Panjang persegi panjang.
        lebar: Lebar persegi panjang.

    Returns:
        Keliling persegi panjang.
    """
    return 2 * (panjang + lebar)


def luas_lingkaran(jari_jari: float) -> float:
    """Menghitung luas lingkaran.

    Args:
        jari_jari: Jari-jari lingkaran.

    Returns:
        Luas lingkaran.
    """
    return PI * jari_jari * jari_jari


def keliling_lingkaran(jari_jari: float) -> float:
    """Menghitung keliling (circumference) lingkaran.

    Args:
        jari_jari: Jari-jari lingkaran.

    Returns:
        Keliling lingkaran.
    """
    return 2 * PI * jari_jari


def celsius_ke_fahrenheit(celsius: float) -> float:
    """Mengonversi suhu dari Celsius ke Fahrenheit.

    Args:
        celsius: Suhu dalam derajat Celsius.

    Returns:
        Suhu dalam derajat Fahrenheit.
    """
    return (celsius * 9 / 5) + 32


def celsius_ke_kelvin(celsius: float) -> float:
    """Mengonversi suhu dari Celsius ke Kelvin.

    Args:
        celsius: Suhu dalam derajat Celsius.

    Returns:
        Suhu dalam Kelvin.
    """
    return celsius + 273.15


if __name__ == "__main__":
    print("Modul math_operations siap digunakan.")