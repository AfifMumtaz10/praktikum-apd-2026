from utils import bersihkan_layar
from tampilan import tampil_menu, lihat_bahan, lihat_akun, error, info
from crud import tambah_bahan, ubah_bahan, hapus_bahan, catat_pemakaian


def menu_admin(akun):
    aksi = {
        "1": lihat_bahan,
        "2": tambah_bahan,
        "3": ubah_bahan,
        "4": hapus_bahan,
        "5": lihat_akun
    }

    while True:
        bersihkan_layar()
        tampil_menu(f"MENU ADMIN - {akun}", [
            ("1", "Lihat Bahan"),
            ("2", "Tambah Bahan"),
            ("3", "Ubah Bahan"),
            ("4", "Hapus Bahan"),
            ("5", "Lihat Daftar Akun"),
            ("0", "Logout"),
        ])

        pilih = input("Pilih menu: ").strip()
        bersihkan_layar()

        if pilih == "0":
            info("Anda telah logout.")
            input("Tekan Enter untuk lanjut...")
            return

        if pilih in aksi:
            aksi[pilih]()
        else:
            error("Pilihan menu tidak tersedia!")

        input("\nTekan Enter untuk lanjut...")


def menu_user(akun):
    aksi = {
        "1": lihat_bahan,
        "2": catat_pemakaian
    }

    while True:
        bersihkan_layar()
        tampil_menu(f"MENU PENGGUNA - {akun}", [
            ("1", "Lihat Bahan"),
            ("2", "Catat Pemakaian Bahan"),
            ("0", "Logout"),
        ])

        pilih = input("Pilih menu: ").strip()
        bersihkan_layar()

        if pilih == "0":
            info("Anda telah logout.")
            input("Tekan Enter untuk lanjut...")
            return

        if pilih in aksi:
            aksi[pilih]()
        else:
            error("Pilihan menu tidak tersedia!")

        input("\nTekan Enter untuk lanjut...")