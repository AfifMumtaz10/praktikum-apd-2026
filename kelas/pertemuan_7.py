# def hitung():
#     return 5 * 3

# print(hitung())

#studi kasus 1
# def hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas):
#     nilai_akhir = (nilai_tugas * 0.20) + (nilai_uts * 0.30) + (nilai_uas * 0.50)
#     return nilai_akhir

# tugas = float(input("Masukkan nilai tugas: "))
# uts = float(input("Masukkan nilai UTS: "))
# uas = float(input("Masukkan nilai UAS: "))

# hasil = hitung_nilai_akhir(tugas, uts, uas)

# print("Nilai akhir siswa:", hasil)

#studi kasus 2
daftar_tugas = []

def tambah_tugas():
    tugas = input("Masukkan judul tugas: ")
    daftar_tugas.append(tugas)
    print("Tugas berhasil ditambahkan!")

def tampilkan_tugas():
    print("\nDaftar Tugas Harian:")
    if len(daftar_tugas) == 0:
        print("Belum ada tugas yang tersimpan.")
    else:
        for i, tugas in enumerate(daftar_tugas, start=1):
            print(f"{i}. {tugas}")
            
tambah_tugas()
tambah_tugas()
tampilkan_tugas()