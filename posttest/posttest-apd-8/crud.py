from data import data_bahan
from utils import minta_teks, minta_angka, temukan_bahan
from tampilan import (
    lihat_bahan, judul, sukses, error, info, pilih_opsi, konfirmasi
)

BATAL = "__batal__"


def pilih_bahan():
    if not data_bahan:
        info("Tidak ada bahan yang tersedia.")
        return None

    pilihan = [
        (f"{nomor}. {nama}", nama)
        for nomor, nama in enumerate(data_bahan, start=1)
    ]
    pilihan.append(("Batal", BATAL))

    hasil = pilih_opsi("Pilih bahan", pilihan)

    if hasil is None or hasil == BATAL:
        return None

    return hasil


def tambah_bahan():
    judul("TAMBAH BAHAN")

    nama = minta_teks("Nama bahan: ")

    if temukan_bahan(nama) is not None:
        error("Bahan sudah terdaftar!")
        return

    sisa = minta_angka("Sisa stok: ")
    satuan = minta_teks("Satuan: ")
    minggu = minta_angka("Minggu ke-: ")
    batas = minta_angka("Batas minimal: ")

    if minggu < 1:
        error("Minggu harus minimal 1.")
        return

    data_bahan[nama] = {
        "sisa": sisa,
        "satuan": satuan,
        "minggu": minggu,
        "batas": batas
    }

    sukses("Bahan berhasil ditambahkan!")


def ubah_bahan():
    judul("UBAH BAHAN")
    lihat_bahan()

    if not data_bahan:
        return

    nama_lama = pilih_bahan()

    if nama_lama is None:
        info("Pengubahan dibatalkan.")
        return

    bahan = data_bahan[nama_lama]
    nama_baru = input("Nama baru (Enter = tetap): ").strip()

    if nama_baru:
        nama_terdaftar = temukan_bahan(nama_baru)

        if nama_terdaftar not in (None, nama_lama):
            error("Nama bahan sudah digunakan.")
        else:
            data_bahan_baru = {}

            for nama, isi in data_bahan.items():
                data_bahan_baru[
                    nama_baru if nama == nama_lama else nama
                ] = isi

            data_bahan.clear()
            data_bahan.update(data_bahan_baru)

    for kunci, label in [
        ("sisa", "Sisa baru"),
        ("minggu", "Minggu baru"),
        ("batas", "Batas minimal baru")
    ]:
        isian = input(f"{label}: ").strip()

        if isian:
            if isian.isdigit():
                nilai = int(isian)

                if kunci == "minggu" and nilai < 1:
                    error("Minggu harus minimal 1.")
                else:
                    bahan[kunci] = nilai
            else:
                error("Input harus berupa angka bulat.")

    satuan_baru = input("Satuan baru (Enter = tetap): ").strip()

    if satuan_baru:
        bahan["satuan"] = satuan_baru

    sukses("Proses pengubahan selesai.")


def hapus_bahan():
    judul("HAPUS BAHAN")
    lihat_bahan()

    if not data_bahan:
        return

    nama = pilih_bahan()

    if nama is None:
        info("Penghapusan dibatalkan.")
        return

    if konfirmasi(f"Hapus '{nama}'?"):
        data_bahan.pop(nama)
        sukses("Bahan berhasil dihapus!")
    else:
        info("Penghapusan dibatalkan.")


def catat_pemakaian():
    judul("CATAT PEMAKAIAN BAHAN")
    lihat_bahan()

    if not data_bahan:
        return

    nama = pilih_bahan()

    if nama is None:
        info("Pencatatan dibatalkan.")
        return

    bahan = data_bahan[nama]
    dipakai = minta_angka(f"Jumlah {nama} yang dipakai: ")

    if dipakai == 0:
        error("Jumlah pemakaian harus lebih dari 0.")
    elif dipakai > bahan["sisa"]:
        error("Pemakaian melebihi sisa stok!")
    else:
        bahan["sisa"] -= dipakai
        sukses(
            f"Pemakaian berhasil dicatat. "
            f"Sisa {nama}: {bahan['sisa']} {bahan['satuan']}."
        )