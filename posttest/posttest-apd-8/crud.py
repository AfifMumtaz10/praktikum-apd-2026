from data import data_bahan
from utils import minta_teks, minta_angka, temukan_bahan
from tampilan import lihat_bahan, judul, sukses, error, info


def pilih_bahan():
    if not data_bahan:
        info("Tidak ada bahan yang tersedia.")
        return None

    nomor = minta_angka("Nomor bahan (0 = batal): ")

    if nomor == 0:
        return None

    if nomor < 1 or nomor > len(data_bahan):
        error("Nomor di luar daftar!")
        return pilih_bahan()

    return list(data_bahan.keys())[nomor - 1]


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

def hapus_bahan():
    judul("HAPUS BAHAN")
    lihat_bahan()

    if not data_bahan:
        return

    nama = pilih_bahan()

    if nama is None:
        info("Penghapusan dibatalkan.")
        return

    yakin = input(f"Hapus '{nama}'? (y/n): ").strip().lower()

    if yakin == "y":
        data_bahan.pop(nama)
        sukses("Bahan berhasil dihapus!")
    elif yakin == "n":
        info("Penghapusan dibatalkan.")
    else:
        error("Masukkan y atau n.")


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