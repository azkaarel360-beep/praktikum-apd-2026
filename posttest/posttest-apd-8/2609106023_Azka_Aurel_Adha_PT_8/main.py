import time
import storage
from create import buat_akun_baru
from login import autentikasi_login
from admin import menu_admin
from user import menu_user
from read import tampilkan_menu_awal

while True:
    pilihan = tampilkan_menu_awal()

    if pilihan == "1":
        username_aktif = autentikasi_login()

        if username_aktif != "":
            if username_aktif.lower() == storage.username_admin.lower():
                menu_admin()
            else:
                menu_user()

    elif pilihan == "2":
        buat_akun_baru()

    elif pilihan == "3":
        print("\nTerima kasih dan sampai jumpa!")
        time.sleep(3)
        break
