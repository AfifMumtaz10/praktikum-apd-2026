print("=" * 30)
print("Program Makanan Bergizi Gratis")
print("=" * 30)

username_benar = "apip"
password_benar = "2609106069"

percobaan = 0
login_berhasil = False

while percobaan < 3:
    print("SILAHKAN LOGIN")
    username = input("Masukkan username: ").lower()
    password = input("Masukkan password: ")

    if username == "":
        print("USERNAME TIDAK BOLEH KOSONG!!")
        continue

    if password == "":
        print("PASSWORD TIDAK BOLEH KOSONG!!")
        continue

    if username == username_benar and password == password_benar:
        print("LOGIN BERHASIL!!")
        login_berhasil = True
        break

    elif username != username_benar and password == password_benar:
        print("USERNAME SALAH!!")

    elif username == username_benar and password != password_benar:
        print("PASSWORD SALAH!!")

    else:
        print("USERNAME DAN PASSWORD SALAH!!")

    percobaan = percobaan + 1
    print("SISA PERC0BAAN LOGIN:", 3 - percobaan)

if login_berhasil == False:
    print("ANDA TELAH MELEWATI BATAS PERC0BAAN LOGIN!! SILAHKAN COBA MINGGU DEPAN!!")

else:
    while True:
        print("=" * 30)
        print("MENU DISTRIBUSI PAKET")
        print("=" * 30)
        print("1. Paket Reguler 1 porsi makanan")
        print("2. Paket Anak 1 porsi makanan")
        print("3. Paket Keluarga 4 porsi makanan")
        print("4. Keluar dari program")

        pilihan = input("Masukkan pilihan Anda (1-4): ")

        if pilihan == "1":
            jenis_paket = "Paket Reguler"
            porsi_per_paket = 1

        elif pilihan == "2":
            jenis_paket = "Paket Anak"
            porsi_per_paket = 1

        elif pilihan == "3":
            jenis_paket = "Paket Keluarga"
            porsi_per_paket = 4

        elif pilihan == "4":
            print("Terima kasih telah menggunakan program ini.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih antara 1-4.")
            continue

        jumlah_paket = int(input("Masukkan Jumlah Paket: "))
        total_porsi = 0

        for i in range(jumlah_paket):
            total_porsi = total_porsi + porsi_per_paket

        jumlah_penerima = total_porsi

        if total_porsi >=20:
            bonus = "5 Paket Buah"

        elif total_porsi >= 10:
            bonus = "3 Botol Susu"

        elif total_porsi >= 5:
            bonus = "1 Paket Vitamin"

        else:
            bonus = "Tidak Mendapatkan Bonus"

        print("=" * 30)
        print("HASIL DISTRIBUSI PAKET")
        print("=" * 30)
        print("Jenis Paket:", jenis_paket)
        print("Jumlah Paket:", jumlah_paket)
        print("Total Porsi:", total_porsi, "porsi")
        print("Penerima Manfaat:", jumlah_penerima, "orang")
        print("Bonus:", bonus)
        print("=" * 30)