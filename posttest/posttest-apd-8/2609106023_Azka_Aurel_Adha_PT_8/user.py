import time
import inquirer
import storage
from storage import cari_lagu, playlist, katalog, username_aktif
from read import tampilkan_katalog, tampilkan_playlist_user
import os

def menu_user():
    if username_aktif not in playlist:
        playlist[username_aktif] = {}
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        pertanyaan = [
            inquirer.List(
                "menu",
                message="=== MENU USER ===",
                choices=[
                    "1. Buat playlist",
                    "2. Lihat playlist",
                    "3. Tambah lagu ke playlist",
                    "4. Hapus lagu dari playlist",
                    "5. Logout"
                ]
            )
        ]
        jawaban = inquirer.prompt(pertanyaan)
        menu = jawaban["menu"]

        if menu == "1. Buat playlist":
            nama_playlist = input("\nNama playlist Anda: ")
            nama_sama = False
            for nama in playlist[username_aktif]:
                if nama.lower() == nama_playlist.lower():
                    nama_sama = True
            
            if nama_playlist == "":
                print("\nNama playlist tidak boleh kosong.")
            elif nama_sama:
                print("\nNama playlist itu sudah ada.")
            else:
                playlist[username_aktif][nama_playlist] = {}
                print("\nPlaylist berhasil dibuat!")
            input("Enter untuk kembali...")
        
        elif menu == "2. Lihat playlist":
            tampilkan_playlist_user()
            input("\nEnter untuk kembali...")
        
        elif menu == "3. Tambah lagu ke playlist":
            print("\n=== PILIH PLAYLIST ===")
            for nama_playlist in playlist[username_aktif]:
                print("-", nama_playlist)
            nama_pilih = input("\nNama playlist tujuan: ")
            nama_asli = ""
            for nama in playlist[username_aktif]:
                if nama.lower() == nama_pilih.lower():
                    nama_asli = nama
            
            if nama_asli == "":
                print("\nPlaylist tidak ditemukan.")
            else:
                tampilkan_katalog()
                judul_tambah = cari_lagu(input("\nJudul lagu yang ingin ditambahkan: "))
            
                if judul_tambah == "":
                    print("\nJudul lagu tidak ditemukan.")
                elif judul_tambah in playlist[username_aktif][nama_asli]:
                    print("\nLagu sudah ada di playlist.")
                else:
                    playlist[username_aktif][nama_asli][judul_tambah] = True
                    print("\nLagu berhasil ditambahkan.")
            input("Enter untuk kembali...")
        
        elif menu == "4. Hapus lagu dari playlist":
            print("\n=== PILIH PLAYLIST ===")
            for nama_playlist in playlist[username_aktif]:
                print("-", nama_playlist)
        
            nama_pilih = input("\nNama playlist tujuan: ")
            nama_asli = ""
            for nama in playlist[username_aktif]:
                if nama.lower() == nama_pilih.lower():
                    nama_asli = nama
        
            if nama_asli == "":
                print("\nPlaylist tidak ditemukan.")
            else:
                print("\nLagu di playlist", nama_asli)
                for judul_lagu in playlist[username_aktif][nama_asli]:
                    judul_asli = cari_lagu(judul_lagu)
                    if judul_asli != "":
                        print(judul_asli, "-", katalog[judul_asli]["penyanyi"], "-", katalog[judul_asli]["genre"])
                judul_hapus_input = input("\nJudul lagu yang ingin dihapus: ")
                
                if judul_hapus_input == "":
                    print("\nJudul lagu tidak boleh kosong.")
                else:
                    judul_hapus = ""
                    for judul in playlist[username_aktif][nama_asli]:
                        if judul.lower() == judul_hapus_input.lower():
                            judul_hapus = judul
                
                    if judul_hapus == "":
                        print("\nJudul lagu tidak ada di playlist.")
                    else:
                        del playlist[username_aktif][nama_asli][judul_hapus]
                        print("\nLagu telah dihapus dari playlist.")
            input("Enter untuk kembali...")
        
        elif menu == "5. Logout":
            print("\nTerima kasih dan sampai jumpa!.")
            time.sleep(3)
            break
        else:
            print("Pilihan tidak tersedia.")
            input("Enter untuk kembali...")