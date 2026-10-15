# kartu = ["merah", "merah", "biru", "hijau"]
# print(kartu)

# set_baru = set(kartu)
# print(set_baru)

# # set menggunakan list
# matkul = ["apd", "orsikom", "apd", "kalkulus"]
# sks = set(matkul)
# print(sks)

# angka_ganjil = {1, 3, 5, 7, 9}
# for angka in angka_ganjil:
#     print(angka)

# kartu = ["merah", "merah", "biru", "hijau"]
# set_kartu = set(kartu)
# set_kartu.add("kuning")

# print(set_kartu)

# kartu = ["merah", "merah", "biru", "hijau"]
# set_kartu = set(kartu)
# print(set_kartu)

# for warna in set_kartu:
#     print(warna)
#     break

# if warna == "merah":
#     print("warna merah ada di set_kartu")
# else:
#     print("warna merah tidak ada di set_kartu")
# set_kartu.add("kuning") 
# print(set_kartu)

# set_kartu.discard("biru")
# print(set_kartu)
# for i in set_kartu:
#     print(i)

# aslab1 = {"fina", "shasha", "risma"}
# aslab2 = {"larry", "attar", "haekal"}
# gabung = aslab1.union(aslab2)
# print(gabung)

# Dictionary
# Biodata = {
# "Nama" : "Siti Julpa",
# "NIM" : 25091060,
# "KRS" : ["Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Instagram" : "julpatarr"
# }

# print(Biodata["Instagram"])
# print(Biodata["KRS"][0])
# print(Biodata.get("Nama"))
# print(f"Nama Instagram saya adalah {Biodata.get('Instagram')}")

# game = {
# "pou" : "chill",
# "genshin impact" : "action",
# "valorant" : "fps",
# "minecraft" : "sandbox",
# "mobile legend" : "moba"
# }
# game["resident evil"] = "horror" #menambahkan data baru secara langsung
# game.update({"resident evil" : "horror", "ML" : "Moba"}) #menggunakan update untuk menambahkan data baru
# game.setdefault("resident evil", "SERAM") #menambahkan data baru, jika key sudah ada, maka values nya tetap pake yang awal
# print(game)

# game_baru = game.pop("valorant") #menghapus data tertentu
# print(game)
# print(game_baru)
# print(len(game))
# game.clear() #menghapus semua data di dictionary
# print(game)


# for i in game:
#     print(i)
# for i in game.keys():
#     print(i)
# for i in game.values():
#     print(i)

# for keys, values in game.items():
#     print(f"{keys} adalah jenis game {values}")

# menu = {
# "ayam geprek" : 15000,
# "ayam goreng" : 13000,
# "ayam bakar" : 17000,
# "nasi goreng" : 12000,
# "mie goreng" : 10000
# }
# menu_baru = menu.copy()
# menu_baru["nasi goreng"] = 15000
# print(menu)
# print(menu_baru)

# key = "ayam geprek", "ayam goreng", "ayam bakar",
# value = 12000
# menu = dict.fromkeys(key, value)
# print(menu)

# menu = {
# "ayam" : ["ayam geprek", "ayam goreng", "ayam bakar"],
# "nasi" : ["nasi goreng", "nasi uduk"],
# "mie" : ["mie goreng rendang", "mie goreng aceh"],
# "kuah" : ["soto", "rawon", "sop iga"]
# }
# for i, j in menu.items():
#     print(f"Kategori {i} memiliki menu :")
# for kategori in j:
#     print(kategori)
# print("")

# data_siswa = {
#     "siswa1":{
#         "nama" : "Johan",
#         "kelas" : "A2",
#         "nilai" : 95
#     },
#     "siswa2":{
#         "nama" : "Niyah",
#         "kelas" : "A2",
#         "nilai" : 90
#     }
# }

# aslab1 = {"fina", "shasha", "risma", "attar"}
# aslab2 = {"larry", "attar", "haekal"}
# print(aslab1.union(aslab2))

# import os
# import time

# print("Hello, GeeksforGeeks!")
# print("This text will be cleared.")

# time.sleep(3)
# os.system("cls")

# print("Screen cleared successfully.")
playlist = []

id_lagu_berikutnya = 4
while True:
    print("Lagu berhasil ditambahkan dengan ID", id_lagu_berikutnya)
    id_lagu_berikutnya += 1

    input("Tekan Enter untuk kembali...")
