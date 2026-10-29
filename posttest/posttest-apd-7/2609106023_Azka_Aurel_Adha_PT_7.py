import os
import time

akun = {"admin": "admin232"}
username_admin = "admin"
katalog = {
    "Tarot": {"penyanyi": "Hindia", "genre": "Pop"},
    "Keep You Safe": {"penyanyi": "Yahya", "genre": "Pop Acoustic"},
    "Keep Me": {"penyanyi": "Novo Amor", "genre": "Indie"}
}
playlist = {}
username_aktif = ""

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
    print("=== MENU AWAL ===")
    print("1. Login")
    print("2. Registrasi")
    print("3. Keluar")
    pilihan = input_menu()

    if pilihan in [1,2,3]:
        return str(pilihan)
    else:
        print("\nPilihan tidak tersedia.")
        input("Enter untuk kembali...")
        return tampilkan_menu_awal()


def validasi_input(teks):
    return teks != ""

def cari_lagu(judul_cari):
    for judul in katalog:
        if judul.lower() == judul_cari.lower():
            return judul
    return ""

def tampilkan_katalog():
    print("\n=== KATALOG LAGU ===")
    if len(katalog) == 0:
        print("Katalog masih kosong.")
    else:
        for judul in katalog:
            print(judul, "-", katalog[judul]["penyanyi"], "-", katalog[judul]["genre"])

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

def tampilkan_playlist_user():
    print("\n=== PLAYLIST SAYA ===")
    ada_playlist = False
    for nama_playlist in playlist[username_aktif]:
        ada_playlist = True
        print("\nPlaylist:", nama_playlist)
        if len(playlist[username_aktif][nama_playlist]) == 0:
            print("Playlist Anda belum ada lagu.")
        for judul_lagu in playlist[username_aktif][nama_playlist]:
            judul_asli = cari_lagu(judul_lagu)
            if judul_asli != "":
                print(judul_asli, "-", katalog[judul_asli]["penyanyi"], "-", katalog[judul_asli]["genre"])
    if ada_playlist == False:
        print("\nKamu belum membuat playlist.")

while True:
    pilihan = tampilkan_menu_awal()
    if pilihan == "1":
        username = input("\nSilahkan masukkan username: ")
        password = input("Silahkan masukkan password: ")
        nama_login = ""
        for nama_akun in akun:
            if username.lower() == nama_akun.lower() and password == akun[nama_akun]:
                nama_login = nama_akun
                break

        if nama_login == "":
            print("\nUsername atau password salah.")
            input("Enter untuk kembali...")
            continue

        username_aktif = nama_login

        if username_aktif.lower() == username_admin.lower():
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print("Login berhasil")
                print("\n=== MENU ADMIN ===")
                print("1. Tambah lagu ke katalog")
                print("2. Lihat katalog")
                print("3. Update katalog lagu")
                print("4. Hapus lagu dari katalog")
                print("5. Logout")
                menu = input("\nPilih menu: ")

                if menu == "1":
                    tambah_lagu_katalog()
                    input("\nEnter untuk kembali...")

                elif menu == "2":
                    tampilkan_katalog()
                    input("\nEnter untuk kembali...")

                elif menu == "3":
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

                elif menu == "4":
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

                elif menu == "5":
                    print("\nTerima kasih dan sampai jumpa!.")
                    time.sleep(3)
                    break
                else:
                    print("\nPilihan tidak tersedia.")
                    input("Enter untuk kembali...")
        else:
            if username_aktif not in playlist:
                playlist[username_aktif] = {}
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print("Login berhasil")
                print("\n=== MENU USER ===")
                print("1. Buat playlist")
                print("2. Lihat playlist")
                print("3. Tambah lagu ke playlist")
                print("4. Hapus lagu dari playlist")
                print("5. Logout")
                menu = input("\nPilih menu: ")

                if menu == "1":
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
                    
                elif menu == "2":
                    tampilkan_playlist_user()
                    input("\nEnter untuk kembali...")

                elif menu == "3":
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

                elif menu == "4":
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

                elif menu == "5":
                    print("\nTerima kasih dan sampai jumpa!.")
                    time.sleep(3)
                    break
                else:
                    print("Pilihan tidak tersedia.")
                    input("Enter untuk kembali...")

    elif pilihan == "2":
        username_baru = input("\nBuat username: ")
        password_baru = input("Buat password: ")
        if username_baru == "" or password_baru == "":
            print("\nUsername dan password tidak boleh kosong.")
        else: 
            username_sama = False
            for nama in akun:
                if nama.lower() == username_baru.lower():
                    username_sama = True

            if username_sama == True:
                print("\nUsername sudah digunakan.")
            else:
                akun[username_baru] = password_baru
                playlist[username_baru] = {}
                print("\nRegistrasi berhasil! Silakan login.")
        input("Enter untuk kembali...")

    elif pilihan == "3":
        print("\nTerima kasih dan sampai jump!")
        time.sleep(3)
        break