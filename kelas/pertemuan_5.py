# studi kasus1
data_harian = ["Senin", 36.5, "Selasa", 37.1, "Rabu", 36.8, "Kamis", 37.0, "Jumat", 36.6]
suhu = data_harian[1::2]
print(suhu)


# studi kasus2
profil_karakter = ("Arthur", 50, True, ["Pedang Suci", "Tameng Naga"])
profil_karakter = profil_karakter[::-1]
print(profil_karakter)

formula1 = ["Suzuka", 10, True, 20.30, ["Lewis Hamilton", 2, 2.50]]
print(formula1)

line_up = [
["Ferrari", "Leclerc", 16],
["Mercedes", "Hamilton", 44],
["Red Bull", "Verstappen", 1],
["McLaren", "Norris", 4]
]
print(line_up[3][0])

for i in line_up:
    for j in i:
        print(j)