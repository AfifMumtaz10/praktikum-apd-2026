import questionary
from colorama import Fore, Style
from prettytable import PrettyTable, TableStyle
from data import data_akun, data_bahan

GAYA_PILIHAN = questionary.Style([
    ("pointer", "fg:#00ffff bold"),
    ("highlighted", "fg:#00ffff bold"),
    ("answer", "fg:#00ffff bold"),
])


def warna(teks, kode):
    return Style.BRIGHT + kode + teks + Style.RESET_ALL


def cyan(teks):
    return warna(teks, Fore.LIGHTCYAN_EX)


def hijau(teks):
    return warna(teks, Fore.LIGHTGREEN_EX)


def merah(teks):
    return warna(teks, Fore.LIGHTRED_EX)


def kuning(teks):
    return warna(teks, Fore.LIGHTYELLOW_EX)


def sukses(teks):
    print(hijau(teks))


def error(teks):
    print(merah("Error: " + teks))


def info(teks):
    print(kuning(teks))


def judul(teks):
    garis = "=" * (len(teks) + 10)
    print(garis)
    print(cyan(teks.center(len(garis))))
    print(garis)


def buat_tabel(teks_judul, kolom, rata_kiri=()):
    tabel = PrettyTable()
    tabel.set_style(TableStyle.DOUBLE_BORDER)
    tabel.title = cyan(teks_judul)
    tabel.field_names = [cyan(nama) for nama in kolom]

    for nama in kolom:
        if nama in rata_kiri:
            tabel.align[cyan(nama)] = "l"

    return tabel


def pilih_opsi(pertanyaan, daftar_pilihan):
    pilihan = [
        questionary.Choice(title=label, value=nilai)
        for label, nilai in daftar_pilihan
    ]

    return questionary.select(
        pertanyaan,
        choices=pilihan,
        qmark="",
        pointer="»",
        instruction=" ",
        style=GAYA_PILIHAN,
    ).ask()


def pilih_menu(teks_judul, daftar_opsi):
    judul(teks_judul)

    hasil = pilih_opsi(
        "",
        [(label, kode) for kode, label in daftar_opsi]
    )

    return hasil if hasil is not None else "0"


def konfirmasi(pertanyaan):
    hasil = pilih_opsi(pertanyaan, [("Tidak", False), ("Ya", True)])
    return hasil is True


def lihat_bahan():
    if not data_bahan:
        info("Belum ada data bahan.")
        return

    kolom = ["No", "Bahan", "Sisa", "Satuan", "Minggu", "Batas", "Keterangan"]
    tabel = buat_tabel("DAFTAR SISA STOK BAHAN MAKANAN KOS", kolom, ["Bahan"])

    for nomor, (nama, bahan) in enumerate(data_bahan.items(), start=1):
        if bahan["sisa"] <= bahan["batas"]:
            sisa = merah(str(bahan["sisa"]))
            keterangan = merah("MENIPIS!")
        else:
            sisa = hijau(str(bahan["sisa"]))
            keterangan = hijau("Aman")

        tabel.add_row([
            nomor, nama, sisa, bahan["satuan"],
            bahan["minggu"], bahan["batas"], keterangan
        ])

    print(tabel)


def lihat_akun():
    kolom = ["No", "Nama Pengguna", "Peran"]
    tabel = buat_tabel("DAFTAR AKUN", kolom, ["Nama Pengguna"])

    for nomor, (nama, info_akun) in enumerate(data_akun.items(), start=1):
        tabel.add_row([nomor, nama, info_akun["peran"]])

    print(tabel)