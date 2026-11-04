import inquirer
from prettytable import PrettyTable
from storage import katalog, playlist, username_aktif, cari_lagu
import os

def input_menu():
    try:
        pilihan = int(input("Silahkan pilih menu (1/2/3): "))
        return pilihan
    except ValueError:
        print("\nInput harus berupa angka 1, 2, atau 3.")
        input("Enter untuk kembali...")
        return 0

def tampilkan_menu_awal():
    os.system("cls" if os.name == "nt" else "clear")
    pertanyaan = [ 
        inquirer.List(
            "pilihan",
            message="=== MENU AWAL ===",
            choices=[
                "1. Login",
                "2. Registrasi",
                "3. Keluar"
            ]
        )
    ]
    jawaban = inquirer.prompt(pertanyaan)
    pilihan = jawaban["pilihan"]

    return pilihan[0] 

def tampilkan_katalog():
    print("\n=== KATALOG LAGU ===")
    if len(katalog) == 0:
        print("Katalog masih kosong.")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["Judul", "Penyanyi", "Genre"]
        for judul in katalog:
            tabel.add_row([judul, katalog[judul]["penyanyi"], katalog[judul]["genre"]])
        print(tabel)

def tampilkan_playlist_user():
    print("\n=== PLAYLIST SAYA ===")
    ada_playlist = False
    for nama_playlist in playlist[username_aktif]:
        ada_playlist = True
        print("\nPlaylist:", nama_playlist)
        if len(playlist[username_aktif][nama_playlist]) == 0:
            print("Playlist Anda belum ada lagu.")
        else:
            tabel = PrettyTable()
            tabel.field_names = ["Judul", "Penyanyi", "Genre"]
            for judul_lagu in playlist[username_aktif][nama_playlist]:
                judul_asli = cari_lagu(judul_lagu)
                if judul_asli != "":
                    tabel.add_row([judul_asli, katalog[judul_asli]["penyanyi"], katalog[judul_asli]["genre"]])
            print(tabel)
    if ada_playlist == False:
        print("\nKamu belum membuat playlist.")