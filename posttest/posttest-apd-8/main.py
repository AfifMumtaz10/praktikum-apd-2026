from colorama import init
from data import data_akun
from utils import bersihkan_layar
from tampilan import pilih_menu, info
from auth import masuk, daftar_akun
from menu import menu_admin, menu_user


def program_utama():
    while True:
        bersihkan_layar()
        pilih = pilih_menu("SISTEM INFORMASI SISA STOK BAHAN MAKANAN KOS MINGGUAN", [
            ("1", "Login"),
            ("2", "Register"),
            ("0", "Keluar"),
        ])
        bersihkan_layar()

        if pilih == "1":
            akun = masuk()

            if akun is not None:
                input("Tekan Enter untuk masuk ke menu...")

                if data_akun[akun]["peran"] == "admin":
                    menu_admin(akun)
                else:
                    menu_user(akun)

        elif pilih == "2":
            daftar_akun()
            input("\nTekan Enter untuk lanjut...")

        elif pilih == "0":
            info("Terima kasih, program selesai.")
            break


if __name__ == "__main__":
    init(autoreset=True)
    program_utama()