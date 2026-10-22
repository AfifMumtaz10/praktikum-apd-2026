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
    """Mengembalikan nama akun (key) di dictionary, atau None jika tidak ada."""
    for nama in data_akun.keys():
        if nama.lower() == nama_pengguna.lower():
            return nama
    return None


def temukan_bahan(nama_bahan):
    """Mengembalikan nama bahan (key) di dictionary, atau None jika tidak ada."""
    for nama in data_bahan.keys():
        if nama.lower() == nama_bahan.lower():
            return nama
    return None


def pilih_bahan():
    """Mengembalikan nama bahan (key) di dictionary, atau None jika dibatalkan."""
    nomor = minta_angka("Nomor bahan (0 = batal): ")
    while nomor < 0 or nomor > len(data_bahan):
        print("Nomor di luar daftar!")
        nomor = minta_angka("Nomor bahan (0 = batal): ")
    if nomor == 0:
        return None
    return list(data_bahan.keys())[nomor - 1]


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
    for nomor, (nama, b) in enumerate(data_bahan.items(), start=1):
        ket = "MENIPIS!" if b["sisa"] <= b["batas"] else "Aman"
        print(f"{nomor:<4}{nama:<20}{b['sisa']:<8}{b['satuan']:<10}{b['minggu']:<8}{ket}")
    print("-" * 74)


def lihat_akun():
    print("=" * 40)
    print("DAFTAR AKUN")
    print("=" * 40)
    print(f"{'No':<4}{'Nama Pengguna':<20}{'Peran'}")
    print("-" * 40)
    for nomor, (nama, info) in enumerate(data_akun.items(), start=1):
        print(f"{nomor:<4}{nama:<20}{info['peran']}")


def tambah_bahan():
    print("--- TAMBAH BAHAN ---")
    nama = minta_teks("Nama bahan:")
    if temukan_bahan(nama) is not None:
        print("Bahan sudah terdaftar, silakan gunakan menu ubah.")
        return
    sisa = minta_angka("Sisa stok: ")
    satuan = minta_teks("Satuan: ")
    minggu = minta_angka("Minggu ke-: ")
    batas = minta_angka("Batas minimal: ")
    data_bahan.update({nama: {"sisa": sisa, "satuan": satuan, "minggu": minggu, "batas": batas}})
    print("Bahan berhasil ditambahkan!")


def ubah_bahan():
    print("--- UBAH BAHAN ---")
    lihat_bahan()
    if not data_bahan:
        return
    nama_lama = pilih_bahan()
    if nama_lama is None:
        print("Dibatalkan.")
        return
    bahan = data_bahan.get(nama_lama)
    print(f"Mengubah: {nama_lama} (Enter = tidak diubah)")

    baru = input("Nama baru: ").strip()
    if baru:
        if temukan_bahan(baru) not in (None, nama_lama):
            print("Nama bahan sudah terdaftar, nama lama dipertahankan.")
        else:
            # ganti key tanpa mengubah urutan data
            isi_baru = {}
            for nama, isi in data_bahan.items():
                isi_baru[baru if nama == nama_lama else nama] = isi
            data_bahan.clear()
            data_bahan.update(isi_baru)

    for kunci, label in [("sisa", "Sisa baru"), ("minggu", "Minggu baru"), ("batas", "Batas minimal baru")]:
        isian = input(f"{label:<19}: ").strip()
        if isian:
            if isian.isdigit():
                bahan[kunci] = int(isian)
            else:
                print(f"{label} tidak valid, nilai lama dipertahankan.")

    baru = input("Satuan baru: ").strip()
    if baru:
        bahan["satuan"] = baru
    print("Bahan berhasil diperbarui!")


def catat_pemakaian():
    print("--- CATAT PEMAKAIAN BAHAN ---")
    lihat_bahan()
    if not data_bahan:
        return
    nama = pilih_bahan()
    if nama is None:
        print("Dibatalkan.")
        return
    bahan = data_bahan.get(nama)
    dipakai = minta_angka(f"Jumlah {nama} yang dipakai: ")
    if dipakai > bahan["sisa"]:
        print("Gagal! Jumlah pemakaian melebihi sisa stok.")
    else:
        bahan["sisa"] -= dipakai
        print(f"Tercatat. Sisa {nama} sekarang {bahan['sisa']} {bahan['satuan']}.")


def hapus_bahan():
    print("--- HAPUS BAHAN ---")
    lihat_bahan()
    if not data_bahan:
        return
    nama = pilih_bahan()
    if nama is None:
        print("Dibatalkan.")
        return
    yakin = input(f"Hapus '{nama}'? (y/n): ").strip().lower()
    if yakin == "y":
        data_bahan.pop(nama)
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

    data_akun.update({nama: {"sandi": sandi, "peran": "user"}})
    print("Registrasi berhasil, silakan login.")


def masuk():
    print("--- LOGIN ---")
    for sisa in range(2, -1, -1):
        nama = minta_teks("Nama pengguna: ")
        sandi = minta_teks("Kata sandi: ")
        akun = temukan_akun(nama)
        if akun is not None and data_akun[akun]["sandi"] == sandi:
            print(f"Login berhasil. Halo, {akun} ({data_akun[akun]['peran']})!")
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
        print(f"  MENU ADMIN - {akun}")
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
        print(f"  MENU PENGGUNA - {akun}")
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
                if data_akun[akun]["peran"] == "admin":
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