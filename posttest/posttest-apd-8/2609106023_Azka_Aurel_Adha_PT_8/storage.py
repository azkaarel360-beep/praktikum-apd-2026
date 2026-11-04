akun = {"admin": "admin232"}

username_admin = "admin"

katalog = {
    "Tarot": {"penyanyi": "Hindia", "genre": "Pop"},
    "Keep You Safe": {"penyanyi": "Yahya", "genre": "Pop Acoustic"},
    "Keep Me": {"penyanyi": "Novo Amor", "genre": "Indie"}
}

playlist = {}
username_aktif = ""

def cari_lagu(judul_cari):
    for judul in katalog:
        if judul.lower() == judul_cari.lower():
            return judul
    return ""