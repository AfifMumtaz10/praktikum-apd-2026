from colorama import Fore, Style
from prettytable import PrettyTable
from data import data_akun, data_bahan


def sukses(teks):
    print(Fore.GREEN + teks + Style.RESET_ALL)


def error(teks):
    print(Fore.RED + "Error: " + teks + Style.RESET_ALL)


def info(teks):
    print(Fore.YELLOW + teks + Style.RESET_ALL)


def judul(teks):
    garis = "=" * len(teks)
    print(Fore.CYAN + Style.BRIGHT + garis)
    print(teks)
    print(garis + Style.RESET_ALL)


def tampil_menu(teks_judul, daftar_opsi):
    judul(teks_judul)

    tabel = PrettyTable()
    tabel.field_names = ["Kode", "Menu"]
    tabel.align["Menu"] = "l"

    for kode, label in daftar_opsi:
        tabel.add_row([kode, label])

    print(tabel)


def lihat_bahan():
    judul("DAFTAR SISA STOK BAHAN MAKANAN KOS")

    if not data_bahan:
        info("Belum ada data bahan.")
        return

    tabel = PrettyTable()
    tabel.field_names = [
        "No", "Bahan", "Sisa", "Satuan", "Minggu", "Batas", "Keterangan"
    ]
    tabel.align["Bahan"] = "l"

    for nomor, (nama, bahan) in enumerate(data_bahan.items(), start=1):
        if bahan["sisa"] <= bahan["batas"]:
            keterangan = Fore.RED + "MENIPIS!" + Style.RESET_ALL
        else:
            keterangan = Fore.GREEN + "Aman" + Style.RESET_ALL

        tabel.add_row([
            nomor, nama, bahan["sisa"], bahan["satuan"],
            bahan["minggu"], bahan["batas"], keterangan
        ])

    print(tabel)


def lihat_akun():
    judul("DAFTAR AKUN")

    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Pengguna", "Peran"]
    tabel.align["Nama Pengguna"] = "l"

    for nomor, (nama, info_akun) in enumerate(data_akun.items(), start=1):
        tabel.add_row([nomor, nama, info_akun["peran"]])

    print(tabel)