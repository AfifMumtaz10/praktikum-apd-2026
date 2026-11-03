from data import data_akun, BATAS_LOGIN
from utils import minta_teks, minta_sandi, temukan_akun
from tampilan import judul, sukses, error, info

jumlah_login_gagal = 0


def daftar_akun():
    judul("REGISTER")

    nama = minta_teks("Nama pengguna: ")

    while " " in nama or temukan_akun(nama) is not None:
        if " " in nama:
            error("Nama pengguna tidak boleh memakai spasi!")
        else:
            error("Nama pengguna sudah digunakan!")

        nama = minta_teks("Nama pengguna: ")

    sandi = minta_sandi("Kata sandi: ")

    while len(sandi) < 4:
        error("Kata sandi minimal 4 karakter!")
        sandi = minta_sandi("Kata sandi: ")

    data_akun[nama] = {
        "sandi": sandi,
        "peran": "user"
    }

    sukses("Registrasi berhasil. Silakan login.")


def masuk():
    global jumlah_login_gagal

    judul("LOGIN")

    for percobaan in range(BATAS_LOGIN):
        nama = minta_teks("Nama pengguna: ")
        sandi = minta_sandi("Kata sandi: ")
        akun = temukan_akun(nama)

        if akun is not None and data_akun[akun]["sandi"] == sandi:
            sukses(
                f"Login berhasil. Halo, {akun} "
                f"({data_akun[akun]['peran']})!"
            )
            return akun

        jumlah_login_gagal += 1
        sisa_percobaan = BATAS_LOGIN - percobaan - 1
        error(f"Data login salah. Sisa percobaan: {sisa_percobaan}")

    info("Percobaan login habis.")
    return None