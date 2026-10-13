import os

data_akun = [
    ["apip", "apip123", "admin"],
    ["salsa", "salsa123", "admin"],
    ["noni", "noni123", "user"],]


data_bahan = [
    ["Beras", 10, "kg", 1, 3],
    ["Telur", 20, "butir", 1, 6],
    ["Mie Instan", 15, "bungkus", 1, 5],
    ["Minyak Goreng", 2, "liter", 1, 1],]


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def tunggu():
    input("\nTekan Enter untuk lanjut...")


def minta_teks(pertanyaan):
    jawaban = input(pertanyaan).strip()
    while jawaban == "":
        print("Isian tidak boleh kosong!")
        jawaban = input(pertanyaan).strip()
    return jawaban


def minta_angka(pertanyaan):
    jawaban = input(pertanyaan).strip()
    while not jawaban.isdigit():
        print("Isian harus berupa angka bulat tidak negatif!")
        jawaban = input(pertanyaan).strip()
    return int(jawaban)


def temukan_akun(nama_pengguna):
    for akun in data_akun:
        if akun[0].lower() == nama_pengguna.lower():
            return akun
    return None


def temukan_bahan(nama_bahan):
    for posisi, bahan in enumerate(data_bahan):
        if bahan[0].lower() == nama_bahan.lower():
            return posisi
    return -1


def pilih_bahan():
    """Mengembalikan posisi bahan di list, atau -1 jika dibatalkan."""
    nomor = minta_angka("Nomor bahan (0 = batal): ")
    while nomor < 0 or nomor > len(data_bahan):
        print("Nomor di luar daftar!")
        nomor = minta_angka("Nomor bahan (0 = batal): ")
    return nomor - 1


def lihat_bahan():
    garis = "=" * 74
    print(garis)
    print("DAFTAR SISA STOK BAHAN MAKANAN KOS")
    print(garis)
    if not data_bahan:
        print("Belum ada data bahan.")
        return
    print(f"{'No':<4}{'Bahan':<20}{'Sisa':<8}{'Satuan':<10}{'Minggu':<8}{'Keterangan'}")
    print("-" * 74)
    for nomor, b in enumerate(data_bahan, start=1):
        ket = "MENIPIS!" if b[1] <= b[4] else "Aman"
        print(f"{nomor:<4}{b[0]:<20}{b[1]:<8}{b[2]:<10}{b[3]:<8}{ket}")
    print("-" * 74)


def lihat_akun():
    print("=" * 40)
    print("DAFTAR AKUN")
    print("=" * 40)
    print(f"{'No':<4}{'Nama Pengguna':<20}{'Peran'}")
    print("-" * 40)
    for nomor, akun in enumerate(data_akun, start=1):
        print(f"{nomor:<4}{akun[0]:<20}{akun[2]}")


def tambah_bahan():
    print("--- TAMBAH BAHAN ---")
    nama = minta_teks("Nama bahan:")
    if temukan_bahan(nama) != -1:
        print("Bahan sudah terdaftar, silakan gunakan menu ubah.")
        return
    sisa = minta_angka("Sisa stok: ")
    satuan = minta_teks("Satuan: ")
    minggu = minta_angka("Minggu ke-: ")
    batas = minta_angka("Batas minimal: ")
    data_bahan.append([nama, sisa, satuan, minggu, batas])
    print("Bahan berhasil ditambahkan!")


def ubah_bahan():
    print("--- UBAH BAHAN ---")
    lihat_bahan()
    if not data_bahan:
        return
    posisi = pilih_bahan()
    if posisi == -1:
        print("Dibatalkan.")
        return
    bahan = data_bahan[posisi]
    print(f"Mengubah: {bahan[0]} (Enter = tidak diubah)")

    baru = input("Nama baru: ").strip()
    if baru:
        bahan[0] = baru

    for indeks, label in [(1, "Sisa baru"), (3, "Minggu baru"), (4, "Batas minimal baru")]:
        isian = input(f"{label:<19}: ").strip()
        if isian:
            if isian.isdigit():
                bahan[indeks] = int(isian)
            else:
                print(f"{label} tidak valid, nilai lama dipertahankan.")

    baru = input("Satuan baru: ").strip()
    if baru:
        bahan[2] = baru
    print("Bahan berhasil diperbarui!")


def catat_pemakaian():
    print("--- CATAT PEMAKAIAN BAHAN ---")
    lihat_bahan()
    if not data_bahan:
        return
    posisi = pilih_bahan()
    if posisi == -1:
        print("Dibatalkan.")
        return
    bahan = data_bahan[posisi]
    dipakai = minta_angka(f"Jumlah {bahan[0]} yang dipakai: ")
    if dipakai > bahan[1]:
        print("Gagal! Jumlah pemakaian melebihi sisa stok.")
    else:
        bahan[1] -= dipakai
        print(f"Tercatat. Sisa {bahan[0]} sekarang {bahan[1]} {bahan[2]}.")


def hapus_bahan():
    print("--- HAPUS BAHAN ---")
    lihat_bahan()
    if not data_bahan:
        return
    posisi = pilih_bahan()
    if posisi == -1:
        print("Dibatalkan.")
        return
    yakin = input(f"Hapus '{data_bahan[posisi][0]}'? (y/n): ").strip().lower()
    if yakin == "y":
        del data_bahan[posisi]
        print("Bahan berhasil dihapus!")
    else:
        print("Penghapusan dibatalkan.")


def daftar_akun():
    print("--- REGISTER ---")
    nama = minta_teks("Nama pengguna: ")
    while " " in nama or temukan_akun(nama) is not None:
        if " " in nama:
            print("Nama pengguna tidak boleh memakai spasi!")
        else:
            print("Nama pengguna sudah dipakai!")
        nama = minta_teks("Nama pengguna : ")

    sandi = minta_teks("Kata sandi    : ")
    while len(sandi) < 4:
        print("Kata sandi minimal 4 karakter!")
        sandi = minta_teks("Kata sandi    : ")

    data_akun.append([nama, sandi, "user"])
    print("Registrasi berhasil, silakan login.")


def masuk():
    print("--- LOGIN ---")
    for sisa in range(2, -1, -1):
        nama = minta_teks("Nama pengguna: ")
        sandi = minta_teks("Kata sandi: ")
        akun = temukan_akun(nama)
        if akun is not None and akun[1] == sandi:
            print(f"Login berhasil. Halo, {akun[0]} ({akun[2]})!")
            return akun
        print(f"Data salah! Sisa percobaan: {sisa}")
    print("Percobaan habis.")
    return None

def menu_admin(akun):
    aksi = {
        "1": lihat_bahan,
        "2": tambah_bahan,
        "3": ubah_bahan,
        "4": hapus_bahan,
        "5": lihat_akun,
    }
    while True:
        bersihkan_layar()
        print("=" * 40)
        print(f"  MENU ADMIN - {akun[0]}")
        print("=" * 40)
        print("1. Lihat Bahan")
        print("2. Tambah Bahan")
        print("3. Ubah Bahan")
        print("4. Hapus Bahan")
        print("5. Lihat Daftar Akun")
        print("0. Logout")
        pilih = input("Pilih: ").strip()
        bersihkan_layar()
        if pilih == "0":
            print("Anda telah logout.")
            tunggu()
            return
        elif pilih in aksi:
            aksi[pilih]()
        else:
            print("Pilihan tidak tersedia!")
        tunggu()


def menu_user(akun):
    aksi = {
        "1": lihat_bahan,
        "2": catat_pemakaian,
    }
    while True:
        bersihkan_layar()
        print("=" * 40)
        print(f"  MENU PENGGUNA - {akun[0]}")
        print("=" * 40)
        print("1. Lihat Bahan")
        print("2. Catat Pemakaian Bahan")
        print("0. Logout")
        pilih = input("Pilih: ").strip()
        bersihkan_layar()
        if pilih == "0":
            print("Anda telah logout.")
            tunggu()
            return
        elif pilih in aksi:
            aksi[pilih]()
        else:
            print("Pilihan tidak tersedia!")
        tunggu()


def program_utama():
    while True:
        bersihkan_layar()
        print("=" * 56)
        print(" SISTEM INFORMASI SISA STOK BAHAN MAKANAN KOS MINGGUAN")
        print("=" * 56)
        print("1. Login")
        print("2. Register")
        print("0. Keluar")
        pilih = input("Pilih: ").strip()
        bersihkan_layar()
        if pilih == "1":
            akun = masuk()
            if akun is not None:
                tunggu()
                if akun[2] == "admin":
                    menu_admin(akun)
                else:
                    menu_user(akun)
                continue
        elif pilih == "2":
            daftar_akun()
        elif pilih == "0":
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak tersedia!")
        tunggu()


program_utama()