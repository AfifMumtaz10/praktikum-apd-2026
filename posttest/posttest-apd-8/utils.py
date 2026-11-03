import os
import pwinput
from data import data_akun, data_bahan
from tampilan import error


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def minta_teks(pertanyaan):
    jawaban = input(pertanyaan).strip()

    if jawaban == "":
        error("Isian tidak boleh kosong!")
        return minta_teks(pertanyaan)

    return jawaban


def minta_sandi(pertanyaan):
    jawaban = pwinput.pwinput(pertanyaan, mask="*").strip()

    if jawaban == "":
        error("Isian tidak boleh kosong!")
        return minta_sandi(pertanyaan)

    return jawaban


def minta_angka(pertanyaan):
    jawaban = input(pertanyaan).strip()

    if not jawaban.isdigit():
        error("Masukkan angka bulat tidak negatif!")
        return minta_angka(pertanyaan)

    return int(jawaban)


def temukan_akun(nama_pengguna):
    for nama in data_akun:
        if nama.lower() == nama_pengguna.lower():
            return nama
    return None


def temukan_bahan(nama_bahan):
    for nama in data_bahan:
        if nama.lower() == nama_bahan.lower():
            return nama
    return None