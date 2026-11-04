import time
import inquirer
import storage
from storage import cari_lagu, playlist, katalog, username_admin
from read import tampilkan_katalog
import os

def tambah_lagu_katalog():
    judul = input("\nJudul lagu: ")
    penyanyi = input("Penyanyi: ")
    genre = input("Genre: ")
    if judul == "" or penyanyi == "" or genre == "":
        print("\nInput tidak boleh kosong.")
    elif cari_lagu(judul) != "":
        print("\nJudul lagu sudah ada di katalog.")
    else:
        katalog[judul] = {"penyanyi": penyanyi, "genre": genre}
        print("\nLagu berhasil ditambahkan.")

def menu_admin():
    if storage.username_aktif.lower() == username_admin.lower():
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            pertanyaan = [
                inquirer.List(
                    "menu",
                    message="=== MENU ADMIN ===",
                    choices=[
                        "1. Tambah lagu ke katalog",
                        "2. Lihat katalog",
                        "3. Update katalog lagu",
                        "4. Hapus lagu dari katalog",
                        "5. Logout"
                    ]
                )
            ]
            jawaban = inquirer.prompt(pertanyaan)
            menu = jawaban["menu"]

            if menu == "1. Tambah lagu ke katalog":
                tambah_lagu_katalog()
                input("\nEnter untuk kembali...")

            elif menu == "2. Lihat katalog":
                tampilkan_katalog()
                input("\nEnter untuk kembali...")
            
            elif menu == "3. Update katalog lagu":
                tampilkan_katalog()
                if len(katalog) > 0:
                    judul_lama = cari_lagu(input("\nMasukkan judul lagu yang ingin diubah: "))
                    if judul_lama == "":
                        print("\nJudul lagu tidak ditemukan.")
                    else:
                        print("\nKosongkan bagian jika tidak ingin mengubahnya.")
                        judul_baru = input(f"Judul baru untuk {judul_lama}: ")
                        penyanyi_baru = input(f"Penyanyi baru untuk {katalog[judul_lama]['penyanyi']}: ")
                        genre_baru = input(f"Genre baru untuk {katalog[judul_lama]['genre']}: ")
                
                        judul_akhir = judul_lama
                        if judul_baru != "":
                            judul_cocok = cari_lagu(judul_baru) 
                        else:
                            judul_cocok = ""
                            
                        if judul_cocok != "" and judul_cocok != judul_lama:
                            print("\nJudul lagu tersebut sudah ada di katalog.")
                        else:
                            if judul_baru != "" and judul_baru != judul_lama:
                                katalog[judul_baru] = katalog[judul_lama]
                                del katalog[judul_lama]
                                judul_akhir = judul_baru
                                for data_user in playlist:
                                    for nama_playlist in playlist[data_user]:
                                        if judul_lama in playlist[data_user][nama_playlist]:
                                            playlist[data_user][nama_playlist][judul_baru] = True
                                            del playlist[data_user][nama_playlist][judul_lama]
                            
                            if penyanyi_baru != "":
                                katalog[judul_akhir]["penyanyi"] = penyanyi_baru
                            if genre_baru != "":
                                katalog[judul_akhir]["genre"] = genre_baru
                            if judul_baru != "" or penyanyi_baru != "" or genre_baru != "":
                                print("\nData lagu berhasil diperbarui.")
                            else:
                                print("\nTidak ada yang diperbarui.")
                input("\nTekan Enter untuk kembali...")
            
            elif menu == "4. Hapus lagu dari katalog":
                tampilkan_katalog()
                if len(katalog) > 0:
                    judul_hapus = cari_lagu(input("\nMasukkan judul lagu yang ingin dihapus: "))
                    if judul_hapus == "":
                        print("\nJudul lagu tidak ditemukan.")
                    else:
                        del katalog[judul_hapus]
                        for data_user in playlist:
                            for nama_playlist in playlist[data_user]:
                                if judul_hapus in playlist[data_user][nama_playlist]:
                                    del playlist[data_user][nama_playlist][judul_hapus]
                        print("\nLagu berhasil dihapus dari katalog.")
                input("Enter untuk kembali...")
            
            elif menu == "5. Logout":
                print("\nTerima kasih dan sampai jumpa!.")
                time.sleep(3)
                break
            else:
                print("\nPilihan tidak tersedia.")
                input("Enter untuk kembali...")