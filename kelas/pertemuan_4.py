# batas = 5
# for i in range(batas):
#     print("Perulangan ke-", i)

# game = ["Genshin", 7.0, True]
# for i in game:
#     print(i)

# for i in range(1, 10):
#     print(i)

# for i in range(1, 3):# Mengontrol baris dalam tabel perkalian
#     for j in range(1, 4):# Mengontrol kolom dalam tabel perkalian
#         print(f'{i} x {j} = {i * j}')
#     print('') #biar ada jarak tiap iterasi

# jawab = "ya"
# hitung = 0

# while(jawab == "ya"):
#     hitung += 1
#     jawab = input("Ulang lagi tidak? ")
# print(f"Total Perulangan : {hitung}")

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# for i in range(20):
#     if i > 12:
#         break
#     print("perulangan ke", i)

# angka_benar = 7

# while True:
#     print("===game tebak angka===")
#     angka_input = int(input("masukkan angka (1-10): "))
#     if angka_benar == angka_input:
#         print("Angka yang anda masukkan benar")
#         break
#     else:
#         print("Angka masih salah")

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

uang = int(input("Masukkan uang saku awal: "))

while uang > 0:
    pengeluaran = int(input("Masukkan nominal pengeluaran: "))

    if pengeluaran <= uang:
        uang -= pengeluaran
        print("Saldo setelah pengeluaran:", uang)
    else:
        print("Saldo tidak mencukupi.")
        break

print("Saldo akhir:", uang)