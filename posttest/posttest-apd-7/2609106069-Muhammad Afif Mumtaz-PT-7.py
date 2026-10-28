
import os

data_akun = {
    "apip": {"sandi": "apip123", "peran": "admin"},
    "salsa": {"sandi": "salsa123", "peran": "admin"},
    "noni": {"sandi": "noni123", "peran": "user"},
}

data_bahan = {
    "Beras": {"sisa": 10, "satuan": "kg", "minggu": 1, "batas": 3},
    "Telur": {"sisa": 20, "satuan": "butir", "minggu": 1, "batas": 6},
    "Mie Instan": {"sisa": 15, "satuan": "bungkus", "minggu": 1, "batas": 5},
    "Minyak Goreng": {"sisa": 2, "satuan": "liter", "minggu": 1, "batas": 1},
}

BATAS_LOGIN = 3
jumlah_login_gagal = 0


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def lihat_bahan():
    print("=" * 74)
    print("DAFTAR SISA STOK BAHAN MAKANAN KOS")
    print("=" * 74)

    if not data_bahan:
        print("Belum ada data bahan.")
        return

    print(f"{'No':<4}{'Bahan':<20}{'Sisa':<8}"
          f"{'Satuan':<10}{'Minggu':<8}{'Keterangan'}")
    print("-" * 74)

    for nomor, (nama, bahan) in enumerate(data_bahan.items(), start=1):
        keterangan = (
            "MENIPIS!" if bahan["sisa"] <= bahan["batas"]
            else "Aman"
        )
        print(
            f"{nomor:<4}{nama:<20}{bahan['sisa']:<8}"
            f"{bahan['satuan']:<10}{bahan['minggu']:<8}"
            f"{keterangan}"
        )

    print("-" * 74)


def lihat_akun():
    print("=" * 40)
    print("DAFTAR AKUN")
    print("=" * 40)
    print(f"{'No':<4}{'Nama Pengguna':<20}{'Peran'}")
    print("-" * 40)

    for nomor, (nama, info) in enumerate(data_akun.items(), start=1):
        print(f"{nomor:<4}{nama:<20}{info['peran']}")


def minta_teks(pertanyaan):
    jawaban = input(pertanyaan).strip()

    if jawaban == "":
        print("Error: Isian tidak boleh kosong!")
        return minta_teks(pertanyaan)

    return jawaban


def minta_angka(pertanyaan):
    jawaban = input(pertanyaan).strip()

    if not jawaban.isdigit():
        print("Error: Masukkan angka bulat tidak negatif!")
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


def pilih_bahan():
    if not data_bahan:
        print("Tidak ada bahan yang tersedia.")
        return None

    nomor = minta_angka("Nomor bahan (0 = batal): ")

    if nomor == 0:
        return None

    if nomor < 1 or nomor > len(data_bahan):
        print("Error: Nomor di luar daftar!")
        return pilih_bahan()

    return list(data_bahan.keys())[nomor - 1]


def tambah_bahan():
    print("--- TAMBAH BAHAN ---")

    nama = minta_teks("Nama bahan: ")

    if temukan_bahan(nama) is not None:
        print("Error: Bahan sudah terdaftar!")
        return

    sisa = minta_angka("Sisa stok: ")
    satuan = minta_teks("Satuan: ")
    minggu = minta_angka("Minggu ke-: ")
    batas = minta_angka("Batas minimal: ")

    if minggu < 1:
        print("Error: Minggu harus minimal 1.")
        return

    data_bahan[nama] = {
        "sisa": sisa,
        "satuan": satuan,
        "minggu": minggu,
        "batas": batas
    }

    print("Bahan berhasil ditambahkan!")


def ubah_bahan():
    print("--- UBAH BAHAN ---")
    lihat_bahan()

    if not data_bahan:
        return

    nama_lama = pilih_bahan()

    if nama_lama is None:
        print("Pengubahan dibatalkan.")
        return

    bahan = data_bahan[nama_lama]
    nama_baru = input("Nama baru (Enter = tetap): ").strip()

    if nama_baru:
        nama_terdaftar = temukan_bahan(nama_baru)

        if nama_terdaftar not in (None, nama_lama):
            print("Error: Nama bahan sudah digunakan.")
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
                    print("Error: Minggu harus minimal 1.")
                else:
                    bahan[kunci] = nilai
            else:
                print("Error: Input harus berupa angka bulat.")

    satuan_baru = input("Satuan baru (Enter = tetap): ").strip()

    if satuan_baru:
        bahan["satuan"] = satuan_baru

    print("Proses pengubahan selesai.")


def hapus_bahan():
    print("--- HAPUS BAHAN ---")
    lihat_bahan()

    if not data_bahan:
        return

    nama = pilih_bahan()

    if nama is None:
        print("Penghapusan dibatalkan.")
        return

    yakin = input(f"Hapus '{nama}'? (y/n): ").strip().lower()

    if yakin == "y":
        data_bahan.pop(nama)
        print("Bahan berhasil dihapus!")
    elif yakin == "n":
        print("Penghapusan dibatalkan.")
    else:
        print("Error: Masukkan y atau n.")


def catat_pemakaian():
    print("--- CATAT PEMAKAIAN BAHAN ---")
    lihat_bahan()

    if not data_bahan:
        return

    nama = pilih_bahan()

    if nama is None:
        print("Pencatatan dibatalkan.")
        return

    bahan = data_bahan[nama]
    dipakai = minta_angka(f"Jumlah {nama} yang dipakai: ")

    if dipakai == 0:
        print("Jumlah pemakaian harus lebih dari 0.")
    elif dipakai > bahan["sisa"]:
        print("Error: Pemakaian melebihi sisa stok!")
    else:
        bahan["sisa"] -= dipakai
        print(
            f"Pemakaian berhasil dicatat. "
            f"Sisa {nama}: {bahan['sisa']} {bahan['satuan']}."
        )


def daftar_akun():
    print("--- REGISTER ---")

    nama = minta_teks("Nama pengguna: ")

    while " " in nama or temukan_akun(nama) is not None:
        if " " in nama:
            print("Error: Nama pengguna tidak boleh memakai spasi!")
        else:
            print("Error: Nama pengguna sudah digunakan!")

        nama = minta_teks("Nama pengguna: ")

    sandi = minta_teks("Kata sandi: ")

    while len(sandi) < 4:
        print("Error: Kata sandi minimal 4 karakter!")
        sandi = minta_teks("Kata sandi: ")

    data_akun[nama] = {
        "sandi": sandi,
        "peran": "user"
    }

    print("Registrasi berhasil. Silakan login.")


def masuk():
    global jumlah_login_gagal

    print("--- LOGIN ---")

    for percobaan in range(BATAS_LOGIN):
        nama = minta_teks("Nama pengguna: ")
        sandi = minta_teks("Kata sandi: ")
        akun = temukan_akun(nama)

        if akun is not None and data_akun[akun]["sandi"] == sandi:
            print(
                f"Login berhasil. Halo, {akun} "
                f"({data_akun[akun]['peran']})!"
            )
            return akun

        jumlah_login_gagal += 1
        sisa_percobaan = BATAS_LOGIN - percobaan - 1
        print(
            f"Error: Data login salah. "
            f"Sisa percobaan: {sisa_percobaan}"
        )

    print("Percobaan login habis.")
    return None


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
        print("=" * 40)
        print(f"MENU ADMIN - {akun}")
        print("=" * 40)
        print("1. Lihat Bahan")
        print("2. Tambah Bahan")
        print("3. Ubah Bahan")
        print("4. Hapus Bahan")
        print("5. Lihat Daftar Akun")
        print("0. Logout")

        pilih = input("Pilih menu: ").strip()
        bersihkan_layar()

        if pilih == "0":
            print("Anda telah logout.")
            input("Tekan Enter untuk lanjut...")
            return

        if pilih in aksi:
            aksi[pilih]()
        else:
            print("Error: Pilihan menu tidak tersedia!")

        input("\nTekan Enter untuk lanjut...")


def menu_user(akun):
    aksi = {
        "1": lihat_bahan,
        "2": catat_pemakaian
    }

    while True:
        bersihkan_layar()
        print("=" * 40)
        print(f"MENU PENGGUNA - {akun}")
        print("=" * 40)
        print("1. Lihat Bahan")
        print("2. Catat Pemakaian Bahan")
        print("0. Logout")

        pilih = input("Pilih menu: ").strip()
        bersihkan_layar()

        if pilih == "0":
            print("Anda telah logout.")
            input("Tekan Enter untuk lanjut...")
            return

        if pilih in aksi:
            aksi[pilih]()
        else:
            print("Error: Pilihan menu tidak tersedia!")

        input("\nTekan Enter untuk lanjut...")


def program_utama():
    while True:
        bersihkan_layar()
        print("=" * 56)
        print("SISTEM INFORMASI SISA STOK BAHAN MAKANAN KOS MINGGUAN")
        print("=" * 56)
        print("1. Login")
        print("2. Register")
        print("0. Keluar")

        pilih = input("Pilih menu: ").strip()
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
            print("Terima kasih, program selesai.")
            break

        else:
            print("Error: Pilihan menu tidak tersedia!")
            input("Tekan Enter untuk lanjut...")


program_utama()