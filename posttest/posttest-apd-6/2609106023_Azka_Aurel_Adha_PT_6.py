import os
import time

akun = {
    "admin": "admin232"
}
username_admin = "admin"

katalog = {
    "Tarot": {
        "penyanyi": "Hindia",
        "genre": "Pop"
    },
    "Keep You Safe": {
        "penyanyi": "Yahya",
        "genre": "Pop Acoustic"
    },
    "Keep Me": {
        "penyanyi": "Novo Amor",
        "genre": "Indie"
    }
}

playlist = {}

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("=== MENU AWAL ===")
    print("1. Login")
    print("2. Registrasi")
    print("3. Keluar")
    pilihan = input("Silahkan pilih menu (1/2/3): ")

    if pilihan == "1":
        username = input("\nSilahkan masukkan username: ")
        password = input("Silahkan masukkan password: ")
        login_berhasil = False

        for nama_akun in akun:
            if username.lower() == nama_akun.lower() and password == akun[nama_akun]:
                login_berhasil = True
                break 

        if login_berhasil == True:
            if username.lower() == username_admin.lower():
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
                        judul = input("\nJudul lagu: ")
                        penyanyi = input("Penyanyi: ")
                        genre = input("Genre: ")

                        if judul == "" or penyanyi == "" or genre == "":
                            print("\nInput tidak boleh kosong.")
                        else:
                            katalog[judul] = {
                                "penyanyi": penyanyi,
                                "genre": genre
                            }
                            print("\nLagu berhasil ditambahkan.")
                        input("Enter untuk kembali...")

                    elif menu == "2":
                        print("\n=== KATALOG LAGU ===")
                        if len(katalog) == 0:
                            print("Katalog masih kosong.")
                        else:
                            for judul in katalog:
                                print(judul, "-", katalog[judul]["penyanyi"], "-", katalog[judul]["genre"])
                        input("\nEnter untuk kembali...")

                    elif menu == "3":
                        print("\n=== UPDATE KATALOG LAGU ===")
                        if len(katalog) == 0:
                            print("Katalog masih kosong.")
                        else:
                            for judul in katalog:
                                print(judul, "-", katalog[judul]["penyanyi"], "-", katalog[judul]["genre"])

                            judul_edit = input("\nMasukkan judul lagu yang ingin diubah: ")
                            ditemukan = False

                            for judul in katalog:
                                if judul.lower() == judul_edit.lower():
                                    print("\nKosongkan bagian jika tidak ingin mengubahnya.")
                                    judul_baru = input(f"\nJudul baru untuk {judul}: ")
                                    penyanyi_baru = input(f"Penyanyi baru untuk {katalog[judul]['penyanyi']}: ")
                                    genre_baru = input(f"Genre baru untuk {katalog[judul]['genre']}: ")

                                    judul_lama = judul
                                    judul_akhir = judul_lama
                                    judul_sama = False

                                    if judul_baru != "":
                                        for judul in katalog:
                                            if judul.lower() == judul_baru.lower():
                                                judul_sama = True

                                    if judul_sama == False:
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
                                        ditemukan = True
                                        break

                            if ditemukan == False:
                                print("\nJudul lagu tidak ditemukan.")
                        input("\nTekan Enter untuk kembali...")


                    elif menu == "4":
                        print("\n=== KATALOG LAGU ===")
                        for judul in katalog:
                            print(judul, "-", katalog[judul]["penyanyi"], "-", katalog[judul]["genre"])

                        judul_hapus = input("\nMasukkan judul lagu yang ingin dihapus: ")
                        ditemukan = False

                        for judul in katalog:
                            if judul.lower() == judul_hapus.lower():
                                del katalog[judul]
                                ditemukan = True
                                break

                        if ditemukan == True:
                            for data_user in playlist:
                                for nama_playlist in playlist[data_user]:
                                    for judul_lagu in playlist[data_user][nama_playlist]:
                                        if judul_lagu.lower() == judul.lower():
                                            del playlist[data_user][nama_playlist][judul_lagu]
                            print("\nLagu berhasil dihapus dari katalog.")
                        else:
                            print("\nJudul lagu tidak ditemukan.")
                        input("Enter untuk kembali...")

                    elif menu == "5":
                        print("\nTerima kasih dan sampai jumpa!.")
                        time.sleep(3)
                        os.system("cls" if os.name == "nt" else "clear")
                        break

                    else:
                        print("\nPilihan tidak tersedia.")
                        input("Enter untuk kembali...")

            else:
                for nama_user in playlist:
                    if nama_user.lower() == username.lower():
                        username = nama_user
                        break

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

                        for data_playlist in playlist[username]:
                            if data_playlist.lower() == nama_playlist.lower():
                                nama_sama = True
                                break
                        
                        if nama_playlist == "":
                            print("\nNama playlist tidak boleh kosong.")
                        elif nama_sama == True:
                            print("\nNama playlist itu sudah ada.")
                        else:
                            playlist[username][nama_playlist] = {}
                            print("\nPlaylist berhasil dibuat!")
                        input("Enter untuk kembali...")

                    elif menu == "2":
                        print("\n=== PLAYLIST SAYA ===")
                        ada_playlist = False

                        for nama_playlist in playlist[username]:
                            ada_playlist = True
                            print("\nPlaylist: ",nama_playlist)

                            if len(playlist[username][nama_playlist]) == 0:
                                print("Playlist Anda belum ada lagu.")
                            for judul_lagu in playlist[username][nama_playlist]:
                                if judul_lagu in katalog:
                                    print(judul_lagu, "-", katalog[judul_lagu]["penyanyi"], "-", katalog[judul_lagu]["genre"])

                        if ada_playlist == False:
                            print("\nKamu belum membuat playlist.")
                        input("Enter untuk kembali...")

                    elif menu == "3":
                        print("\n=== PILIH PLAYLIST ===")
                        for nama_playlist in playlist[username]:
                            print("-", nama_playlist)

                        nama_pilih = input("\nNama playlist tujuan: ")
                        playlist_ditemukan = False

                        for nama_playlist in playlist[username]:
                            if nama_playlist.lower() == nama_pilih.lower():
                                playlist_ditemukan = True

                                print("\n=== KATALOG LAGU ===")
                                for judul in katalog:
                                    print(judul, "-", katalog[judul]["penyanyi"], "-", katalog[judul]["genre"])
                                
                                judul_tambah = input("\nJudul lagu yang ingin ditambahkan: ")
                                lagu_ditemukan = False

                                for judul in katalog:
                                    if judul.lower() == judul_tambah.lower():
                                        lagu_ditemukan = True

                                        if judul not in playlist[username][nama_playlist]:
                                            playlist[username][nama_playlist][judul] = True
                                            print("\nLagu berhasil ditambahkan.")
                                        else:
                                            print("\nLagu sudah ada di playlist.")
                                        break
                                
                                if lagu_ditemukan == False:
                                    print("\nJudul lagu tidak ditemukan.")
                                    break

                        if playlist_ditemukan == False:
                            print("\nPlaylist tidak ditemukan.")
                        input("Enter untuk kembali...")

                    elif menu == "4":
                        print("\n=== PILIH PLAYLIST ===")
                        for nama_playlist in playlist[username]:
                            print("-", nama_playlist)

                        nama_pilih = input("\nNama playlist tujuan: ")
                        playlist_ditemukan = False

                        for nama_playlist in playlist[username]:
                            if nama_playlist.lower() == nama_pilih.lower():
                                playlist_ditemukan = True
                                print("\nLagu di playlist", nama_playlist)

                                for judul_lagu in playlist[username][nama_playlist]:
                                    if judul_lagu in katalog:
                                        print(judul_lagu, "-", katalog[judul_lagu]["penyanyi"], "-", katalog[judul_lagu]["genre"])
                                
                                judul_hapus = input("\nJudul lagu yang ingin dihapus: ")
                                lagu_dihapus = False

                                for judul_lagu in playlist[username][nama_playlist]:
                                    if judul_lagu.lower() == judul_hapus.lower():
                                        del playlist[username][nama_playlist][judul_lagu]
                                        lagu_dihapus = True
                                        break

                                if lagu_dihapus == True:
                                    print("\nLagu telah dihapus dari playlist.")
                                else:
                                    print("\nJudul lagu tidak ada di playlist.")
                                break

                        if playlist_ditemukan == False:
                            print("\nPlaylist tidak ditemukan.")
                        input("Enter untuk kembali...")

                    elif menu == "5":
                        print("\nTerima kasih dan sampai jumpa!.")
                        time.sleep(3)
                        os.system("cls" if os.name == "nt" else "clear")
                        break

                    else:
                        print("Pilihan tidak tersedia.")
                        input("Enter untuk kembali...")

        else:
            print("\nUsername atau password salah.")
            input("Enter untuk kembali...")

    elif pilihan == "2":
        username_baru = input("\nBuat username: ")
        password_baru = input("Buat password: ")

        if username_baru == "" or password_baru == "":
            print("\nUsername dan password tidak boleh kosong.")
            input("Enter untuk kembali...")
        else:
            sudah_ada = False
            for nama_akun in akun:
                if nama_akun.lower() == username_baru.lower():
                    sudah_ada = True
            if sudah_ada == True:
                print("\nUsername sudah digunakan.")
                input("Enter untuk kembali...")
            else:
                akun[username_baru] = password_baru
                playlist[username_baru] = {}
                print("\nRegistrasi berhasil! Silakan login.")
                input("Enter untuk kembali...")

    elif pilihan == "3":
        print("\nTerima kasih dan sampai jumpa!")
        time.sleep(3)
        os.system("cls" if os.name == "nt" else "clear")
        break

    else:
        print("\nPilihan tidak tersedia.")
        input("Enter untuk kembali...")