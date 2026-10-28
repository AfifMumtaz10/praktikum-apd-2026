# studi kasus 1

import random
from datetime import datetime

angka = "012345678910"
pin = "".join(random.choices(angka, k=6))
tanggal = datetime.now().strftime("%d-%m-%y")

print("=== KODE PIN KEAMANAN ===")
print("KODE PIN :", pin)
print("Tanggal dibuat :", tanggal)