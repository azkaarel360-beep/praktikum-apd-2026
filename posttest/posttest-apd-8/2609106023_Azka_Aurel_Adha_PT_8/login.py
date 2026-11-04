import storage

def validasi_input(teks):
    return teks != ""

def autentikasi_login():
    username = input("\nSilahkan masukkan username: ")
    password = input("Silahkan masukkan password: ")
    nama_login = ""
    for nama_akun in storage.akun:
        if username.lower() == nama_akun.lower() and password == storage.akun[nama_akun]:
            nama_login = nama_akun
            break
    if nama_login == "":
        print("\nUsername atau password salah.")
        input("Enter untuk kembali...")
        return ""
            
    storage.username_aktif = nama_login
    return storage.username_aktif