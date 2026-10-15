import os
import time

akun = [
    ["admin", "admin232"]
]
username_admin = "admin"

katalog = [
    ["Tarot", "Hindia", "Pop"],
    ["Keep You Safe", "Yahya", "Pop Acoustic"],
    ["Keep Me", "Novo Amor", "Indie"]
]

playlist = []

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

        for data in akun:
            if username.lower() == data[0].lower() and password == data[1]:
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
                        if judul == "":
                            print("\nInput tidak boleh kosong.")
                            input("Tekan Enter untuk kembali...")
                        else:
                            katalog.append([judul, penyanyi, genre])
                            print("\nLagu berhasil ditambahkan.")
                            input("Tekan Enter untuk kembali...")

                    elif menu == "2":
                        print("\n=== KATALOG LAGU ===")
                        if len(katalog) == 0:
                            print("Katalog masih kosong.")
                        for lagu in katalog:
                            print(lagu[0], "-", lagu[1], "-", lagu[2])
                        input("\nTekan Enter untuk kembali...")

                    elif menu == "3":
                        print("\n=== KATALOG LAGU ===")
                        for lagu in katalog:
                            print(lagu[0], "-", lagu[1], "-", lagu[2])

                        judul_edit = input("\nMasukkan judul lagu yang ingin diubah: ")
                        ditemukan = False

                        for lagu in katalog:
                            if (lagu[0]) == judul_edit:
                                print("\nKosongkan bagian jika tidak ingin mengubahnya.")
                                judul_baru = input(f"Judul baru untuk [{lagu[0]}]: ")
                                penyanyi_baru = input(f"Penyanyi baru untuk [{lagu[0]}]: ")
                                genre_baru = input(f"Genre baru untuk [{lagu[0]}]: ")

                                if judul_baru != "":
                                    judul_lama = lagu[0]
                                    lagu[0] = judul_baru
                                    for data_user in playlist:
                                        for data_playlist in data_user[1]:
                                            if judul_lama in data_playlist[1]:
                                                data_playlist[1].remove(judul_lama)
                                                data_playlist[1].append(judul_baru)
                                if penyanyi_baru != "":
                                    lagu[1] = penyanyi_baru
                                if genre_baru != "":
                                    lagu[2] = genre_baru
                                ditemukan = True
                                print("\nData lagu berhasil diperbarui.")
                                break

                        if ditemukan == False:
                            print("\nJudul lagu tidak ditemukan.")
                        input("Tekan Enter untuk kembali...")

                    elif menu == "4":
                        print("\n=== KATALOG LAGU ===")
                        for lagu in katalog:
                            print(lagu[0], "-", lagu[1], "-", lagu[2])

                        judul_hapus = input("\nMasukkan judul lagu yang ingin dihapus: ")
                        ditemukan = False

                        for lagu in katalog:
                            if (lagu[0]) == judul_hapus:
                                katalog.remove(lagu)
                                ditemukan = True
                                break

                        if ditemukan == True:
                            for data_user in playlist:
                                for data_playlist in data_user[1]:
                                    if (judul_hapus) in data_playlist[1]:
                                        data_playlist[1].remove(judul_hapus)
                            print("\nLagu berhasil dihapus dari katalog.")
                        else:
                            print("\nJudul lagu tidak ditemukan.")
                        input("Tekan Enter untuk kembali...")

                    elif menu == "5":
                        print("\nTerima kasih dan sampai jumpa!.")
                        time.sleep(3)
                        os.system("cls" if os.name == "nt" else "clear")
                        break

                    else:
                        print("Pilihan tidak tersedia.")
                        input("Tekan Enter untuk kembali...")

            else:
                for data_user in playlist:
                    if data_user[0].lower() == username.lower():
                        playlist_user = data_user[1]
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

                        for data_user in playlist:
                            if data_user[0].lower() == username.lower():
                                for data_playlist in data_user[1]:
                                    if data_playlist[0].lower() == nama_playlist.lower():
                                        nama_sama = True

                        if nama_playlist == "":
                            print("\nNama playlist tidak boleh kosong.")
                            input("Tekan Enter untuk kembali...")
                        elif nama_sama == True:
                            print("\nNama playlist itu sudah ada.")
                            input("Tekan Enter untuk kembali...")
                        else:
                            for data_user in playlist:
                                if data_user[0].lower() == username.lower():
                                    data_user[1].append([nama_playlist, []])
                            print("\nPlaylist berhasil dibuat!")
                            input("Tekan Enter untuk kembali...")

                    elif menu == "2":
                        print("\n=== PLAYLIST SAYA ===")
                        ada_playlist = False

                        for data_user in playlist:
                            if data_user[0].lower() == username.lower():
                                for data_playlist in data_user[1]:
                                    ada_playlist = True

                                    print("\nPlaylist: ",data_playlist[0])
                                    if len(data_playlist[1]) == 0:
                                        print("Playlist Anda belum ada lagu.")
                                    for judul_lagu in data_playlist[1]:
                                        for lagu in katalog:
                                            if lagu[0] == judul_lagu:
                                                print(lagu[0], "-", lagu[1], "-", lagu[2])

                        if ada_playlist == False:
                            print("\nKamu belum membuat playlist.")
                        input("Tekan Enter untuk kembali...")

                    elif menu == "3":
                        print("\n=== PILIH PLAYLIST ===")
                        for data_user in playlist:
                            if data_user[0].lower() == username.lower():
                                for data_playlist in data_user[1]:
                                    print("-", data_playlist[0])

                        nama_pilih = input("Nama playlist tujuan: ")
                        playlist_ditemukan = False

                        for data_user in playlist:
                            if data_user[0].lower() == username.lower():
                                for data_playlist in data_user[1]:
                                    if data_playlist[0].lower() == nama_pilih.lower():
                                        playlist_ditemukan = True

                                        print("\n=== KATALOG LAGU ===")
                                        for lagu in katalog:
                                            print(lagu[0], "-", lagu[1], "-", lagu[2])
                                        judul_tambah = input("\nJudul lagu yang ingin ditambahkan: ")
                                        lagu_ditemukan = False

                                        for lagu in katalog:
                                            if (lagu[0]) == judul_tambah:
                                                lagu_ditemukan = True
                                                if lagu[0] not in data_playlist[1]:
                                                    data_playlist[1].append(lagu[0])
                                                    print("\nLagu berhasil ditambahkan.")
                                                else:
                                                    print("\nLagu sudah ada di playlist.")
                                                break
                                        if lagu_ditemukan == False:
                                            print("\nJudul lagu tidak ditemukan.")

                        if playlist_ditemukan == False:
                            print("\nPlaylist tidak ditemukan.")
                        input("Tekan Enter untuk kembali...")

                    elif menu == "4":
                        print("\n=== PILIH PLAYLIST ===")
                        for data_user in playlist:
                            if data_user[0].lower() == username.lower():
                                for data_playlist in data_user[1]:
                                    print("-", data_playlist[0])

                        nama_pilih = input("Nama playlist: ")
                        playlist_ditemukan = False

                        for data_user in playlist:
                            if data_user[0].lower() == username.lower():
                                for data_playlist in data_user[1]:
                                    if data_playlist[0] == nama_pilih:
                                        playlist_ditemukan = True

                                        print("\nLagu di playlist",data_playlist[0])
                                        for judul_lagu in data_playlist[1]:
                                            for lagu in katalog:
                                                if lagu[0] == judul_lagu:
                                                    print(lagu[0], "-", lagu[1], "-", lagu[2])

                                        judul_hapus = input("Judul lagu yang ingin dihapus: ")
                                        lagu_dihapus = False
                                        for judul_lagu in data_playlist[1]:
                                            if (judul_lagu)  == judul_hapus:
                                                data_playlist[1].remove(judul_lagu)
                                                lagu_dihapus = True
                                                break

                                        if lagu_dihapus == True:
                                            print("Lagu telah dihapus dari playlist.")
                                        else:
                                            print("Judul lagu tidak ada di playlist.")
                                        break

                        if playlist_ditemukan == False:
                            print("Playlist tidak ditemukan.")
                        input("Tekan Enter untuk kembali...")

                    elif menu == "5":
                        print("\nTerima kasih dan sampai jumpa!.")
                        time.sleep(3)
                        os.system("cls" if os.name == "nt" else "clear")
                        break

                    else:
                        print("Pilihan tidak tersedia.")
                        input("Tekan Enter untuk kembali...")

        else:
            print("\nUsername atau password salah.")
            input("Tekan Enter untuk kembali...")

    elif pilihan == "2":
        username_baru = input("\nBuat username: ")
        password_baru = input("Buat password: ")

        if username_baru == "" or password_baru == "":
            print("\nUsername dan password tidak boleh kosong.")
            input("Tekan Enter untuk kembali...")
        else:
            sudah_ada = False
            for data in akun:
                if data[0].lower() == username_baru.lower():
                    sudah_ada = True
            if sudah_ada == True:
                print("\nUsername sudah digunakan.")
                input("Tekan Enter untuk kembali...")
            else:
                akun.append([username_baru, password_baru])
                playlist.append([username_baru, []])
                print("\nRegistrasi berhasil! Silakan login.")
                input("Tekan Enter untuk kembali...")

    elif pilihan == "3":
        print("\nTerima kasih dan sampai jumpa!")
        time.sleep(3)
        os.system("cls" if os.name == "nt" else "clear")
        break

    else:
        print("\nPilihan tidak tersedia.")
        input("Tekan Enter untuk kembali...")