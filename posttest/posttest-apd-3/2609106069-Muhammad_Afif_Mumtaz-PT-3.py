nama_benar = "apip parker"
nim_benar = "69"

print("=" * 25)
print("LOGIN GREEN LANTERN CORPS")
print("=" * 25)

nama_input = input("Masukkan nama: ")
nim_input = input("Masukkan 2 Digit NIM: ")

login_berhasil = False

if nama_input == nama_benar:
    if nim_input == nim_benar:
        login_berhasil = True
    else:
        print("[GAGAL]Nama yang anda masukkan salah")
else:
    if nim_input == nim_benar:
        print("[GAGAL]NIM yang anda masukkan salah")
    else:
        print("[GAGAL]Nama dan NIM yang anda masukkan salah")

if login_berhasil:
    print("=" * 40)
    print(f"Login Berhasil, Selamat Datang {nama_benar}")
    print("=" * 40)

    print("         Daftar Misi         ")
    print(" 1.    Misi Standar              (+2%)")
    print(" 2.    Misi Sulit                (+5%)")
    print(" 3.    Misi Kritis               (+8%)")
    print(" 4.    Misi Penyelamatan Bumi    (+12%)")
    print("=" * 40)

    pilihan_misi = input("Masukkan Nomor Pilihan Misi : ")

    reward_dasar = 1000

    if pilihan_misi == "1":
        nama_misi = "Misi Standar"
        persen_bonus = 0.02
    elif pilihan_misi == "2":
        nama_misi = "Misi Sulit"
        persen_bonus = 0.05
    elif pilihan_misi == "3":
        nama_misi = "Misi Kritis"
        persen_bonus = 0.08
    elif pilihan_misi == "4":
        nama_misi = "Misi Penyelamatan Bumi"
        persen_bonus = 0.12
    else:
        nama_misi = "Misi Tidak Tersedia"
        persen_bonus = "Persen Bonus Tidak Tersedia"
    if nama_misi == "Misi Tidak Tersedia":
        print("Misi Tidak Tersedia, Silahkan Pilih Misi Yang Tersedia")
    else:
        reward_bonus = reward_dasar * persen_bonus
        reward_akhir = reward_dasar + reward_bonus

        print("=" * 40)
        print(f"        REWARD MISI {nama_benar}       ")
        print("=" * 40)
        print(f"Nama Misi : {nama_misi}")
        print(f"Reward Dasar : {reward_dasar:.2f} Poin Energi")
        print(f"Reward Bonus : {reward_bonus:.2f} Poin Energi")
        print("=" * 40)
        print(f"Reward Akhir : {reward_akhir:.2f} Poin Energi")
        print("=" * 40)
else:
    print("=" * 40)
    print("Login Gagal, Silahkan Coba Lagi")
    print("=" * 40)